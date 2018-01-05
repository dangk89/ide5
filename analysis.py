import geojson
with open("sf_crime.geojson") as json_file:
    json_data = geojson.load(json_file)


with open("sfpd_districts.geojson") as json_file:
    districts = geojson.load(json_file)
#print json_data[0]

assaults = []
for i in range(10000):
	if json_data[i]['properties']['Category'] == 'NON-CRIMINAL':
		assaults.append(json_data[i])

dates = []
for i in range(len(assaults)):
	dates.append(assaults[i]['properties']['Dates'])

days = []
for i in range(len(assaults)):
	days.append(assaults[i]['properties']['DayOfWeek'])

years = [e[:4] for e in dates]
crimesYear = [(e, years.count(e)) for e in sorted(set(years))]

months = [e[5:7] for e in dates]
crimesMonth = [(e, months.count(e)) for e in sorted(set(months))]

crimesDay = [(e, days.count(e)) for e in sorted(set(days))]
#print(crimesDay)