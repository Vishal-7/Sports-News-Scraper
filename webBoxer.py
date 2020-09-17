import urllib.request, urllib.parse, urllib.error #Importing these to retrieve the webpage html content
from bs4 import BeautifulSoup # importing to scrape the data from the webpage
import ssl # importing to check the certificate of the website
import csv # importing to report the output to a comma seperated file
from datetime import date
link_dict = {}

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE # verifying the certificate
html = urllib.request.urlopen("https://www.indiatoday.in/sports", context=ctx).read() # open the webpage and get the html content of the webpage requested as a request object
soup = BeautifulSoup(html, 'lxml') # parsing the object using beautiful soup to traverse through the html document
today = date.today()
csv_file = open('news_portal_'+str(today)+'.csv','w') # creates a csv file with the write mode to add lines to the file
csv_writer = csv.writer(csv_file,lineterminator='\n') # used to remove the newline in the csv file
csv_writer.writerow(['Article Name','Article Content','Date Posted','Tags','Author'])
top_stories = soup.find('div',class_="special-top-news")
# print(top_stories.prettify())
for i in top_stories.find_all('li',class_=""):
    title = i.attrs['title']
    link = "https://www.indiatoday.in/"+str(i.a.attrs['href'])
    link_dict[title] = link
for n_headlines,n_link in link_dict.items():
    content = []
    tags = []
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE # verifying the certificate
    html = urllib.request.urlopen(n_link, context=ctx).read() # open the webpage and get the html content of the webpage requested as a request object
    soup = BeautifulSoup(html, 'lxml')
    try:
        for i in soup.find_all('span', class_="tag-follow"):
            tags.append(i.a.text)
        final_tags = ",".join(tags)
        date_posted = soup.find('dt', class_="pubdata").text
        posted_by = soup.find('span', class_="posted-name").text
        content_test = soup.find('div',{"itemprop" : "articleBody"}).find_all('p')
        for sample in content_test:
            content.append(sample.text)
        final_content = "".join(content)
    except:
        continue
    csv_writer.writerow([n_headlines,final_content,date_posted,final_tags,posted_by])
csv_file.close()
