import requests as r 
import pandas as pd

# Funcion para pedir datos a la API
def pull_data(sticker,date_from, date_to):
    results = []
    url = 'https://api.polygon.io/v2/aggs/ticker/'
    stock = sticker
    multiplier = "1"
    timespan ="day"
    adjusted ="adjusted=true"
    limit = "40000"
    sort = "sort=desc"
    api_key = '9ovpxCQpe6eGfjKL6UICNwnSxltjIX49'
    
    x = r.get(url+stock+'/range/'+multiplier+'/'+ timespan + '/'+ date_from+ '/'+ date_to +'?'+adjusted+'&'+sort+'&'+limit+'&apiKey='+ api_key)
    y = x.json()
   
    date = 0
    if str(x.status_code)[0] =='4':
        print('Hubo un error')
    else:
        if y['queryCount'] == 0:print('Sin valores')
        else: results = y ['results']
    for value in results:
        value['s'] = sticker
    
    return(results)
   
# Funcion para verifcar que existe la Accion
def check_ticker(name):

    response = r.get('https://api.polygon.io/v3/reference/tickers?ticker='+name+'&active=true&sort=ticker&order=asc&limit=10&apiKey=9ovpxCQpe6eGfjKL6UICNwnSxltjIX49')
    a = response.json()["results"]
    return a



if __name__ == "__main__":
    # sticker = 'AAPL'
    # date_from = '2020-06-01'
    # date_to = '2022-06-17'
    # a = pull_data( sticker, date_from, date_to)
    # print(a)
    pass
    
 