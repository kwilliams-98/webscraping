import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



webpage = 'https://ebible.org/asv/JHN'

#dynamically build the URL to get random chapters. 21 chapters in John (so 1-22). numbers below 0 get a PageNotFoundError

chapter = random.randint(1,21)

if chapter <10: 
    chapter = '0'+ str(chapter)
else:
    chapter = str(chapter)

webpage = webpage + str(chapter + '.htm')


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

#extract the verses from the page 

verses = soup.findAll('div', class_='main')

for verse in verses:
    verse_list = verse.text.split('.')

# print(verse_list)

myverse = random.choice(verse_list[:len(verse_list)-5]) #don't want to include the last 5 elements of the list! 


#print(f"Chapter:, {chapter}, Verse: {myverse}")
message = "Chapter: " + chapter + ' Verse:' + myverse 

print(message)

# import keys3
# from twilio.rest import Client 

# client = Client(keys3.accountSID, keys3.authToken)

# TwilioNumber = '+13464880814'
# myCellPhone = '+14692617027'

# textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body=message)
# print(textmessage.status)


#WHEN YOU'RE DONE!!! TRY BIBLEHUB!
