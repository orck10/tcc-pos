import csv
import json


earningsListWithESGFile = open("sample2.json")
dataJson = json.load(earningsListWithESGFile)

header = ['name', 'totalCash', 'ebitda', 'totalDebt', 'totalRevenue', 'totalEsg']
datas = []
errors = [] 

for o in dataJson:
    for key in o:
        financial = o[key]["financial"]
        esg = o[key]["esg"]
        if (not 'Quote not found for ticker symbol:' in financial) and (not 'Quote not found for ticker symbol:' in esg) and financial["financialCurrency"] == "USD":
            try:
                totalCash = financial["totalCash"]
                ebitda = financial["ebitda"]
                totalDebt = financial["totalDebt"]
                totalRevenue = financial["totalRevenue"]
                esgTotal = o[key]["esg"]["totalEsg"]
                
                dataList = [key, totalCash, ebitda, totalDebt, totalRevenue, esgTotal]
                datas.append(dataList)
            except:
                errors.append(key)

print(datas)
with open('dados.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerows(datas)


with open("error.txt", "w") as outfile:
    outfile.write(str(errors))
