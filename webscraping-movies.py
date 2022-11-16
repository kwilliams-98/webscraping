
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font


#points of interest for the top 5 movies: rank, movie name, total gross, distributor; average gross per theater (total gross/number of theaters)


#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
print()
print()

movie_rows = soup.findAll("tr")

for x in range(1,6):
    td=movie_rows[x].findAll("td")
    rank = td[0].text
    name = td[1].text
    theaters = int(td[6].text.replace(',',''))
    total_gross = int(td[7].text.replace(',','').replace('$',''))
    distributor = td[9].text

    average_gross = (total_gross/theaters)

    print(f'Rank:{rank}')
    print(f'Movie:{name}')
    print(f'Total Gross:{total_gross:,.2f}')
    print(f'Distributor:{distributor}')
    print(f'Average Gross:{average_gross:,.2f}')

##
##
##
##

