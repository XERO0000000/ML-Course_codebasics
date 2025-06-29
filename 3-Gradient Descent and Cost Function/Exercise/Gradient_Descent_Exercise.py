import joblib
import pandas as pd
import numpy as np
import math

#Gradient Descent for m :
#m_curr = m_curr - learning_rate * md

#Gradient Descent for b :
#b_curr = b_curr - learning_rate * bd

#md equation :
#md = -(2 / n) * sum(x * (y - y_predicted))

#bd equation :
#bd = -(2 / n) * sum(y - y_predicted)


#Gradient Descent function:
def Gradient_Descent(x, y) :
    m_curr = b_curr = 0
    n = len(x)

    iterations = 100000
    learning_rate = 0.0002
    
    cost_previous = 0

    for i in range(iterations) :
        #y_predicted equation:
        y_predicted = m_curr * x + b_curr
        
        #Cost Function :
        cost = (1 / n) * sum([val ** 2 for val in (y - y_predicted)])

        #md equation :
        md = -(2 / n) * sum(x * (y - y_predicted))
        #bd equation :
        bd = -(2 / n) * sum(y - y_predicted)

        #Gradient Descent for m :
        m_curr = m_curr - learning_rate * md
        #Gradient Descent for b :
        b_curr = b_curr - learning_rate * bd

        if math.isclose(cost, cost_previous, rel_tol = 1e-20) :
            break

        cost_previous = cost

        #print("m {}, b {}, cost {}, iterations {}" . format(m_curr, b_curr, cost, i))

    return m_curr, b_curr


if __name__ == "__main__" :
    #Reading the CSV file:
    main_df = pd.read_csv(r"C:\Users\XERO_0000\Desktop\ML-Course_codebasics\3-Gradient Descent and Cost Function\Exercise\test_scores.csv")

    #Importing the math and cs columns from main_df:
    math_column = main_df['math'].values
    cs_column = main_df['cs'].values

    #converting math and cs columns into lists:
    math_list = math_column.tolist()
    cs_list = cs_column.tolist()

    #convert math_column into x and cs_column into y:
    x = np.array(math_list)
    y = np.array(cs_list)

    m, b = Gradient_Descent(x, y)
    
    model = {'m' : m, 'b' : b}
    joblib.dump(model, r"C:\Users\XERO_0000\Desktop\ML-Course_codebasics\3-Gradient Descent and Cost Function\Exercise\Trained_Gradient_Descent_Model.joblib")