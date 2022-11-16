# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

table_rows = soup.findAll("tr") #type in the tag that you're looking for!

#highest death rate, lowest death rate, highest testing rate, lowest testing rate (tr = tablerow, td=tablecell)

# print(type(table_rows)) #still a soup object, but this is an object that is ITERABLE (list)! 

high_death_rate = 0.0
low_death_rate = 100.0
high_test_rate = 0.0
low_test_rate = 100.0

for row in table_rows[2:52]: 
    td = row.findAll('td')
    state = td[1].text
    total_cases = int(td[2].text.replace(',', ""))
    total_deaths = int(td[4].text.replace(',', ""))
    total_tests = int(td[10].text.replace(',', ""))
    population = int(td[12].text.replace(',', ""))

    death_rate = round((total_deaths/total_cases)*100, 2)
    test_rate = round((total_tests/population)*100, 2)

    print(state)
    print('-'*10)
    print(f'Death Rate: {death_rate}')
    print(f'Test Rate: {test_rate}')
    print()
    # input()

    if death_rate >= high_death_rate:
        high_death_rate = death_rate
        high_death_state = state
    if death_rate <= low_death_rate:
        low_death_rate = death_rate
        low_death_state = state
    if test_rate >= high_test_rate:
        high_test_rate = test_rate
        high_test_state = state
    if test_rate <= low_test_rate:
        low_test_rate = test_rate
        low_test_state = state
    

print(f'Highest Death Rate: {high_death_state}{high_death_rate}%')
print()
print(f'Lowest Death Rate: {low_death_state}{low_death_rate}%')
print()
print(f'Highest Test Rate: {high_test_state}{high_test_rate}%')
print()
print(f'Lowest Test Rate: {low_test_state}{low_test_rate}%')
print()
    


#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

