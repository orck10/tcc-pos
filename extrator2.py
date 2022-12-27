from yahooquery import Screener
from yahooquery import Ticker
import json
import time
import threading

not_found = 'No screener records found. Check if scrIds are correct'
s = Screener()
available_screeners = s.available_screeners
list_values = []
symbols = []
lote = []




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
def get_data(s, symbols, earningsListWithESG, errors):
    
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


for s in symbols:
    if(len(lote) == 6) :
        lote.append(s)
        t1 = threading.Thread(target=get_data, args=(lote[0], symbols, earningsListWithESG, errors,))
        t2 = threading.Thread(target=get_data, args=(lote[1], symbols, earningsListWithESG, errors,))
        t3 = threading.Thread(target=get_data, args=(lote[2], symbols, earningsListWithESG, errors,))
        t4 = threading.Thread(target=get_data, args=(lote[3], symbols, earningsListWithESG, errors,))
        t5 = threading.Thread(target=get_data, args=(lote[4], symbols, earningsListWithESG, errors,))
        t6 = threading.Thread(target=get_data, args=(lote[5], symbols, earningsListWithESG, errors,))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        
        lote = []
    else:
        lote.append(s)




json_object = json.dumps(earningsListWithESG, indent=4)

with open("sample2.json", "w") as outfile:
    outfile.write(json_object)


print('Ações')
print(len(earningsListWithESG))
print('Erros')
print(errors)
print('FIM')

