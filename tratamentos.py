import csv
import json


earningsListWithESGFile = open("sample.json")
dataJson = json.load(earningsListWithESGFile)

header = ['name', 'area', 'country_code2', 'country_code3']
datas = []

for o in dataJson:
    for key in o:
        dataO = o[key]
        quartersFinancials = dataO["earning"][key]["financialsChart"]["quarterly"]
        esg = dataO["esg"][key]["totalEsg"]
        
        #dataList = [key, dataO.]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerows(datas)
