from flask import Flask,request,jsonify
import pickle
import numpy as np
model=pickle.load(open('finalized_model1.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return "hello world"
@app.route('/predict',methods=['POST'])
def predict():
    Gender=request.form.get('Gender')
    Married=request.form.get('Married')
    Dependents=request.form.get('Dependents')
    Education=request.form.get('Education')
    Self_Employed=request.form.get('Self_Employed')
    ApplicantIncome=request.form.get('ApplicantIncome')
    CoapplicantIncome=request.form.get('CoapplicantIncome')
    LoanAmount=request.form.get('LoanAmount')
    Loan_Amount_Term=request.form.get('Loan_Amount_Term')
    Credit_History=request.form.get('Credit_History')
    Property_Area=request.form.get('Property_Area')
    if Gender=="Male":
        Gender=1
    else:
        male=0
    if Married=="Yes":
        Married=1
    else:
        Married=0
    if Dependents=='1':
        Dependents=1
    elif Dependents=='2':
        Dependents=2
    else:
        Dependents=3
    if Education=="Graduate":
        Education=1
    else:
        Education=0
    if Self_Employed=="Yes":
        Self_Employed=1
    else:
        Self_Employed=0
    if Property_Area=="Rural":
        Property_Area=1
    elif Property_Area=="Urban":
        Property_Area=2
    else:
        Property_Area=3
    input_query=np.array([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,
    Loan_Amount_Term,Credit_History,Property_Area]])
    result =model.predict(input_query)
    if result==1:
        return jsonify({'Loan_Status':'Yes'})
    else:
        return jsonify({'Loan_Status':'NO'})
if __name__=='__main__':
    app.run(debug=True)