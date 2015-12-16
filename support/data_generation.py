import csv
from random import gauss
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

def get_street_info():
    street = []
    while len(street) < n:
        value = "14th str."
        street.append(value)
    #print street
    return street

def get_city_info():
    city = []
    while len(city) < n:
        value = 'New York'
        city.append(value)
    #print city
    return city

def get_state_info():
    state = []
    while len(state) < n:
        value = "NY"
        state.append(value)
    #print state
    return state

def get_zip():
    zip = []
    while len(zip) < n:
        value = "10009"
        zip.append(value)
    #print zip
    return zip

def get_user_id():
    user_id = []
    while len(user_id) < n:
        value = 11
        user_id.append(value)
    #print user_id
    return user_id

def get_user_pk():
    user_pk = []
    while len(user_pk) < n:
        value = 11
        user_pk.append(int(value))
    return user_pk



def main():
    price = get_price()
    sqFt = get_sqFT()
    year = get_year()
    doorMan = get_doorMan()
    min_away = get_subwayProximity()
    street = get_street_info()
    city = get_city_info()
    state = get_state_info()
    zip = get_zip()
    user_id = get_user_id()
    user_pk = get_user_pk()
    featureset = [[] for x in xrange(n)]
    #featureset[0]= ["city", "zip", "sqFt", "has_doorman","user_pk", "min_from_subway", "state","street", "year"]
    feature_entry = []
    priceset = [[] for x in xrange(n)]
    #priceset[0] = ["price"]
    price_entry = []

    for i in range(n):
        feature_entry.append(city[i])
        feature_entry.append(zip[i])
        feature_entry.append(sqFt[i])
        feature_entry.append(doorMan[i])
        feature_entry.append(user_pk[i])
        feature_entry.append(min_away[i])
        feature_entry.append(state[i])
        feature_entry.append(street[i])
        #feature_entry.append(user_id[i])
        feature_entry.append(year[i])
        featureset[i] = feature_entry
        feature_entry = []
   
    for i in range(n):
        price_entry.append(price[i])
        priceset[i] = price_entry
        price_entry = []

    with open('sub_data.csv', 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(featureset)
        
    with open('price_data.csv','w') as fp:
        b = csv.writer(fp, delimiter=',')
        b.writerows(priceset)
        

if __name__ == "__main__":
    main()
