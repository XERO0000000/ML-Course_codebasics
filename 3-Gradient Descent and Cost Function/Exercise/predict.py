import joblib

#Loading the Model:
model = joblib.load(r"C:\Users\XERO_0000\Desktop\ML-Course_codebasics\3-Gradient Descent and Cost Function\Exercise\Trained_Gradient_Descent_Model.joblib")

#Importing m and b from The Trained Model:
m = model['m']
b = model['b']

#Predict the CS score based on the Math score user inputs:
try:
    x = float(input("Enter the Math score : \n"))
    y_predicted = m * x + b
    print("The CS score is : {}" .format(y_predicted))
except ValueError:
    print("Print a valid numeric value for the Math score")
