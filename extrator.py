from yahooquery import Screener
from yahooquery import Ticker
import json
import time

not_found = 'No screener records found. Check if scrIds are correct'
s = Screener()
available_screeners = s.available_screeners
list_values = []
symbols = []
count = 0




#Obter lista com os simbolos referente as ações das empresas
for a in available_screeners:

    print(str(available_screeners.index(a)) + "/" + str(len(available_screeners)))

    values = s.get_screeners([a], 250)
    if(not not_found in values[a]):
        quotes = values[a]['quotes']
        for q in quotes:
            if symbols.count(q['symbol']) == 0:
                symbols.append(q['symbol'])

earningsListWithESG = []
errors = []


#Obter os dados das ações, levando em consideração os simbolos

for s in symbols:
    
    print(str(symbols.index(s)) + "/" + str(len(symbols)))
    the_ticker  = Ticker(s)
    
    try:
        esg = the_ticker.esg_scores
        financial = the_ticker.financial_data
        obj = {s : {'esg' : esg[s], 'financial' : financial[s]} }
        if esg[s] != 'No fundamentals data found for any of the summaryTypes=esgScores' :
            if not 'No fundamentals data found for any of the' in financial[s] :
                earningsListWithESG.append(obj)
    except:
        errors.append(s)



json_object = json.dumps(earningsListWithESG, indent=4)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)


print('Ações')
print(len(earningsListWithESG))
print('Erros')
print(errors)
print('FIM')

