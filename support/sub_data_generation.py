import csv
from random import gauss
n = 10000

#same city, street, state as these are not factors in the regression model
#these 10k are under user_pk = 2

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
        value = gauss(40, 15)
        value = format(value, '.2f')
        price.append(value)
    price.sort(key=lambda p: float(p))
    return price

def get_year():
    year = []
    while len(year) < n:
        value = gauss(1990, 7)
        if value <= 2015:
            value = round(value, 0)
            year.append(int(value))
    year.sort(key=lambda p: float(p))
    return year

def get_doorMan():
    frac = n/2
    #doorMan is binary
    doorMan = []
    while len(doorMan) < frac:
        value = 0
        doorMan.append(value)
    while len(doorMan) < n:
        value = 1
        doorMan.append(value)
    return doorMan

def get_subwayProximity():
    min_away = []
    while len(min_away) < n:
        value = gauss(20, 10)
        if value > 2:
            value = round(value, 0)
            min_away.append(int(value))
    min_away= sorted(min_away, reverse=True)
    return min_away

def get_street_info():
    street = []
    while len(street) < n:
        value = "14th str."
        street.append(value)
    return street

def get_city_info():
    city = []
    while len(city) < n:
        value = 'New York'
        city.append(value)
    return city

def get_state_info():
    state = []
    while len(state) < n:
        value = "NY"
        state.append(value)
    return state

def get_zip():
    zip = []
    while len(zip) < n:
        value = "10009"
        zip.append(value)
    return zip

def get_user_pk():
    user_pk = []
    while len(user_pk) < n:
        value = 2
        user_pk.append(int(value))
    return user_pk

def main():
    sqFt = get_sqFT()
    year = get_year()
    doorMan = get_doorMan()
    min_away = get_subwayProximity()
    street = get_street_info()
    city = get_city_info()
    state = get_state_info()
    zip = get_zip()
    user_pk = get_user_pk()
    featureset = [[] for x in xrange(n)]
    #featureset[0]= ["city", "zip", "sqFt", "has_doorman","user_pk", "min_from_subway", "state","street", "year"]
    feature_entry = []

    for i in range(n):
        feature_entry.append(city[i])
        feature_entry.append(zip[i])
        feature_entry.append(sqFt[i])
        feature_entry.append(doorMan[i])
        feature_entry.append(user_pk[i])
        feature_entry.append(min_away[i])
        feature_entry.append(state[i])
        feature_entry.append(street[i])
        feature_entry.append(year[i])
        featureset[i] = feature_entry
        feature_entry = []

    with open('sub_data.csv', 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(featureset)
        

if __name__ == "__main__":
    main()
