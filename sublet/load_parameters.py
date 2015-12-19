__author__      = "Emily"

import django
from app.models import Parameters

django.setup()

f = open("parameters.txt", "r")
def load_parameters(file, city):
     f = file
     city = city
     print f
     for line in f:
        x =line.split(' ')
        parameters = Parameters(city = city, intercept = x[0], sqFt_coef = x[1], year_coef = x[2], has_doorman_coef = x[3], min_from_subway_coef = x[4])
        parameters.save()
        
def main():
     load_parameters(f, "new york")

if __name__ == "__main__":
	main()
