import requests
from bs4 import BeautifulSoup

def getHtml():
    url = 'https://eshop-prices.com/?'
    query = 'currency=USD'
    target = url + query

    res = requests.get(target)
    return BeautifulSoup(res.text, 'lxml')

def getRegionName(soup):
    regionList= []
    regions = soup.find('thead').text
    regionList = regions.split(' ')
    return regionList[1:-1]

def getGamePrice(row):
    gamePrice = []
    cols = row.find_all('td')
    for col in cols:
        gamePrice.append(col.text)
    return gamePrice

def matchPriceAndRegion(priceList, regionList):
    # TODO: match price and region before sort
    pass


soup = getHtml()
gameList = []

regionList = getRegionName(soup)
rows = soup.find('table').tbody.find_all('tr')

for idx, row in enumerate(rows):
    # get game's name
    gameName = row.find('th').text
    priceList = getGamePrice(row)
    '''
    for i in range(len(regionList)):
        print(regionList[i] + ': ' + priceList[i])
    '''
    dict = {gameName: gameList}
    gameList.append(dict)

print(gameList)
