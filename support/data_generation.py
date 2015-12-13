from random import gauss
f = open("sub_data.csv", "wb")
n = 10000

def get_sqFT():
	sqFt = []
	while len(sqFt) < n:
		value = gauss(700, 100)
		value = format(value, '.2f')
		sqFt.append(value)
	sqFt.sort(key=lambda p: float(p))
	return sqFt

def get_price():
	price = [] 
	while len(price) < n:
		value = gauss(1000, 100)
		value = format(value, '.2f')
		price.append(value)
	price.sort(key=lambda p: float(p))
	return price

def get_year():
	year = []
	while len(year) < n:
		value = gauss(1990, 7)
		value = round(value, 0)
		year.append(int(value))
	year.sort(key=lambda p: float(p))
	return year

def get_doorMan():
	frac = n/2
	#doorMan is binary 
	doorMan = []
	while len(doorMan) < frac:
		value = 1
		doorMan.append(value)
	while len(doorMan) < n:
		value = 0
		doorMan.append(value)
	return doorMan

def get_subwayProximity():
	min_away = []
	while len(min_away) < n:
		value = gauss(13, 10)
		if value > 0:
			value = round(value, 0)
			min_away.append(int(value))
	min_away= sorted(min_away)
	return min_away

def main():
	price = get_price()
	sqFt = get_sqFT()
	year = get_year()
	doorMan = get_doorMan()
	min_away = get_subwayProximity()
	f.write("%s %s %s %s %s\n"%("price", "sqFt", "year","doorMan","min_from_sub"))
	for i in range(n):
		f.write(str(price[i]) +" "+str(sqFt[i]) + " " + str(year[i]) +" "+str(doorMan[i]) +" " +str(min_away[i])+" " + "\n")


if __name__ == "__main__":
    main()
