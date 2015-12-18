import csv
from django.db.models.loading import get_model
from app.models import *
'''

def dump(qs, outfile_path):
    model = qs.model
    #print model
    writer = csv.writer(open(outfile_path, 'w'))
    headers = {}
    features = ["sqFt", "year", "has_doorman", "min_from_subway"]
    for field in model._meta.fields:
    	i = 1
    	print field.name
    
    	if field.name in features:
    		print field.name
    	
    		headers[i] = field.name
    		i += 1
    print "hearders:"
    print headers
   
 
    	writer.writerow(headers)
	for obj in qs:
		row = []
		for field in headers:
			val = getattr(obj, field)
			if callable(val):
				val = val()
			if type(val) == unicode:
				val = val.encode("utf-8")
			row.append(val)
		writer.writerow(row)
		
'''
qs = ApartmentOwned.objects.filter(city="New York").values_list('id', 'sqFt')
print qs
#dump(qs,'./dump.csv')
