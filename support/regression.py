import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#templates html /Users/yehua/sublet/sublet/app/templates/app
# pip install pandas
# pip install statsmodels
# pip install patsy
f = open("parameters.txt", "wb")
#parse the csv file
def regression(file_name):
    f = file_name
    data = pd.read_csv(f, sep=r"\s+")
    feature_cols = ['sqFt', 'year', 'doorMan', 'min_from_sub']
    X = data[feature_cols]
    y = data.price
    lm = LinearRegression()
    lm.fit(X,y)
    intercept = lm.intercept_
    intercept = format(intercept, '.2f')
    coef_list = lm.coef_
    R_square = lm.score(X, y)
    return intercept, coef_list
def main():
    intercept, coef_list = regression("sub_data.csv")
    f.write(str(intercept) + " ")
    for param in coef_list:
        param = format(param, '.2f')
        f.write(str(param) + " " )
if __name__ == "__main__":
    main()
