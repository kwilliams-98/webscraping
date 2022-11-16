from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://cryptoslate.com/coins/' 

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title
print(title.text)
print('-' * 38)
print()

tablecells = soup.findAll('tr')

#need: name/symbol, current price, % change, previous close? 
#if statement to validate for Bitcoin (under $40000) and Ethereum ($3000)
for row in tablecells[0:6]:
   
    td = row.findAll('td')
    if td:
        rank = td[0].text
        name = td[1].text
        symbol= td[1].text 
        current_price = float(td[2].text.replace('$', '').replace(',',''))
        percent_change = float(td[3].text.replace('.','').replace('%','').replace('+','').replace('-','-'))
        calculated_percent_change = (0.01*percent_change)
        change_price = (current_price * calculated_percent_change) 

        print(rank)
        print('---')
        print('Name:', name.split()[0])
        print(symbol.split()[1])
        print('-'*5)
        print(f"Current Price: ${current_price:,.2f}")
        print(f"Percent Change: {percent_change:,.2f}%")
        print(f"Change Price: ${change_price:,.2f}")
    
    
        if current_price < 400000:
            if current_price > 15000:
                print('Price of Bitcoin is under $40,000. Proceed with caution!')

        if current_price < 3000:
            if current_price > 500:
                print('Price of Ethereum is under $3,000. Proceed with caution!')
        
    
    print()
    print()
  
