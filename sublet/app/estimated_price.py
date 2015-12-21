import os

def getEstimatedPrice(sqFt, year, minsFromSub):
	script_dir = os.path.dirname('parameters.txt')
	print script_dir
	file = open('parameters.txt', 'r')
	parameters = file.read().split()
	price = float(parameters[0]) + float(parameters[1])*int(sqFt) + float(parameters[2])*int(year) + float(parameters[3])*int(minsFromSub)
	return int(price)

p = getEstimatedPrice(1000,1998,10)
print p
