import csv

with open('sub_data.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = ApartmentOwned.objects.get_or_create(
            city = row[0],
            zip = row[1],
            sqFt = row[2],
            has_doorman = row[3],
			user_pk = row[4],
			min_from_subway = row[5],
			state = row[6],
            street = row[7],
            user = row[8],
            year = row[9]

            )
            # creates a tuple of the new object or
            # current object and a boolean of if it was created

'''
"fields": {
    "city": "Stony Brook",
    "zip": "11790",
    "sqFt": 25.0,
    "has_doorman": true,
    "user_pk": 11,
    "min_from_subway": 5,
    "state": "NY",
    "street": "100 Nicolls Road",
    "user": 11,
    "year": 1994
  },
  "model": "app.apartmentowned",
  "pk": 6
'''