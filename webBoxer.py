import urllib.request, urllib.parse, urllib.error #Importing these to retrieve the webpage html content
from bs4 import BeautifulSoup # importing to scrape the data from the webpage
import ssl # importing to check the certificate of the website
import csv # importing to report the output to a comma seperated file
from datetime import date

test_dict = dict()
tag_dict = dict()
link = "https://www.google.com/search?safe=active&biw=820&bih=695&tbs=qdr%3Ad&tbm=nws&sxsrf=ALeKk01hNXjAYnGEs02fdHhZcSPXKYsjoA%3A1600039726396&ei=LqteX47jF4WgsQWE052wCw&q=modi&oq=modi&gs_l=psy-ab.3..0i433k1l2j0l8.145750.146098.0.147011.4.4.0.0.0.0.164.556.0j4.4.0....0...1c.1.64.psy-ab..0.4.553....0.xnA42ZM6Lhk"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE # verifying the certificate
req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'lxml')
today = date.today()
# print(soup.prettify())
for i in soup.find_all('div',class_="ZINbbc xpd O9g5cc uUPGi"):
    link = i.find('a',href=True)['href']
    test_link = link.split("/url?q=")[1]
    final_link = test_link.split("&sa=")[0]
    heading =  (i.find('div',class_="BNeawe vvjwJb AP7Wnd").text)
    passage = i.find('div',class_="BNeawe s3v9rd AP7Wnd").text
    
    print(heading)
    print(final_link)
    print(passage)
    print("----------------------------------------------")
# csv_file = open('news_portal_'+str(today)+'.csv','w') # creates a csv file with the write mode to add lines to the file
# csv_writer = csv.writer(csv_file,lineterminator='\n') # used to remove the newline in the csv file
# csv_writer.writerow(['Article Name','Article Content','Date Posted','Tags','Author'])
# print(soup.prettify())

