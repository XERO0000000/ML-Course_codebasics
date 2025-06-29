import math
import pandas as pd
import numpy as np
from word2number import w2n

def word_to_number(word) :
    word = str(word).lower()

    try :
        return w2n.word_to_num(word)
    except :
        return np.nan

main_df = pd.read_csv(r"C:\Users\XERO_0000\Desktop\ML-Course_codebasics\2-Linear Regression Multiple Variables\hiring.csv")
pure_df = pd.read_csv(r"C:\Users\XERO_0000\Desktop\ML-Course_codebasics\2-Linear Regression Multiple Variables\hiring.csv", usecols = ["experience"])

result = pure_df['experience'].apply(word_to_number)

avg = math.floor(result.mean())
result.fillna(0, inplace = True)


#result.to_csv(r"C:\Users\XERO_0000\Desktop\ML-Course_codebasics\2-Linear Regression Multiple Variables\hiring_cleaned.csv", index = False)

main_df["experience"] = result
test_score_avg = math.floor(main_df['test_score(out of 10)'].mean())
#main_df['test_score(out of 10)'].fillna(test_score_avg, inplace = True)
main_df['test_score(out of 10)'] = main_df['test_score(out of 10)'].fillna(test_score_avg)

main_df.to_csv(r"C:\Users\XERO_0000\Desktop\ML-Course_codebasics\2-Linear Regression Multiple Variables\hiring_cleaned.csv", index = False)