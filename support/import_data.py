#this script in made for testing, not in production
import csv
from app.models import ApartmentOwned

fields = ['user_pk', 'street', 'city', 'state', 'zip', 'user', 'sqFt', 'year', 'has_doorman', 'min_from_subway']
for row in csv.reader(open('sub_data.csv')):
    ApartmenOwned.objects.create(**dict(zip(fields, row)))
