import os

def getEstimatedPrice(sqFt, year, minsFromSub):
	file = open('support/parameters.txt', 'r')
	parameters = file.read().split()
	price = float(parameters[0]) + float(parameters[1])*int(sqFt) + float(parameters[2])*int(year) + float(parameters[3])*int(minsFromSub)
	return int(price)
