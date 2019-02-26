categories_url_template = 'https://data.police.uk/api/crime-categories?date={date}'
resp = requests.get(categories_url_template.format(date = my_date))
if resp.ok:
    categories_json = resp.json()
else:
    print(resp.reasone)

categories = {categ["url"]:categ["name"] for categ in categories_json}
crime_category_stats = dict.fromkeys(categories.keys(), 0)
crime_category_stats.pop("all-crime")
for crime in crimes:
    crime_category_stats[crime["category"]] += 1
pprint(crime_category_stats)
