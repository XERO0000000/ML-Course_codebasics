import numpy as np

#The Equation of Gradient Descent:
#m_new = m_old - learning_rate*(md)
#b_new = b_old - learning_rate*(bd)

#md and bd equation:
#md = -(2 / n) * sum(x * (y - y_predicted))
#bd = -(2 / n) * sum(y - y_predicted)

def Gradien_Descent(x, y):
    #Initialize m_curr and b_curr:
    m_curr = b_curr = 0
    learning_rate = 0.00001
    iterations = 10000
    n = len(x)

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr

        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)

        m_curr = m_curr - learning_rate*(md)
        b_curr = b_curr - learning_rate*(bd)

        print("m{}, b{}, iteration{}".format(m_curr, b_curr, i))
    
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

Gradien_Descent(x, y)