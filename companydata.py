import bs4 as bs
import pickle
import requests

def save_tickers():
    response = requests.get("https://www.slickcharts.com/sp500")
    soup = bs.BeautifulSoup(response.text,"lxml")
    table = soup.find('table', {'class' : 'table table-hover table-borderless table-sm'})
    tkrs = []
    for row in table.findAll('tr')[1:]:
        tkr = row.findAll('td')[2].text
        tkrs.append(tkr)
    with open("sp500tkrs.pkl","wb") as f:
        pickle.dump(tkrs,f)
    print(tkrs)
    return tkrs
save_tickers()    
