# pip install pandas
# pip install statsmodels
# pip install patsy
#this program reads in a csv, parse it to form featureset, and outputs the regression parameter to screen and a file called "parameters.txt"
import django
import csv
from app.models import ListingOwned
from app.models import ApartmentOwned
import pandas as pd
from sklearn.linear_model import LinearRegression
django.setup()
f = open("./support/parameters.txt", "wb")
#parse the csv file
def regression(file_name):
    f = file_name
    data = pd.read_csv(f, sep=r",")
    feature_cols = ['sqFt','year','has_doorman','min_from_subway']
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
    f.write(str(intercept) + " ")
    for param in coef_list:
        param = format(param, '.4f')
        f.write(str(param) + " " )
 
if __name__ == "__main__":
    main()
