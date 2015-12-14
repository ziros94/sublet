import csv
from app.models import ApartmentOwned
# If you're using different field names, change this list accordingly.
# The order must also match the column order in the CSV file.
fields = ['user_pk', 'street', 'city', 'state', 'zip', 'user', 'sqFt', 'year', 'has_doorman', 'min_from_subway']
for row in csv.reader(open('sub_data.csv')):
    Representative.objects.create(**dict(zip(fields, row)))
