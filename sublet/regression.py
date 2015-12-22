# pip install pandas
# pip install statsmodels
# pip install patsy
#this program reads in a csv, parse it to form featureset, and outputs the regression parameter to screen and a file called "parameters.txt"
import django
import sys
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
cur = os.path.dirname(os.path.realpath('__file__'))
sys.path.append(cur)
os.environ["DJANGO_SETTINGS_MODULE"] = "sublet.settings"
django.setup()
#parse the csv file
def regression(file_name):
    f = file_name
    data = pd.read_csv(f, sep=r",")
    feature_cols = ['sqFt','year','min_from_subway']
    X = data[feature_cols]
    y = data.price
    lm = LinearRegression()
    lm.fit(X,y)
    intercept = lm.intercept_
    intercept = format(intercept, '.2f')
    coef_list = lm.coef_
    R_square = lm.score(X, y)
    print "regression result:"
    print intercept, coef_list
    return intercept, coef_list
    
def main():  
    intercept, coef_list = regression("./support/dump.csv")
    f = open("./support/parameters.txt", "wb")
    f.write(str(intercept) + " ")
    for param in coef_list:
        param = format(param, '.4f')
        f.write(str(param) + " " )
    f.close()
if __name__ == "__main__":
    main()
