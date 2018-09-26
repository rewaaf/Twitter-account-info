from bs4 import BeautifulSoup
import requests
username = input('Enter Twitter username: ')
link = requests.get('https://www.twitter.com/' + username)
soup = BeautifulSoup(link.content, 'html.parser')
for item in soup.find_all('li', class_='ProfileNav-item'):
    try:
        print(item.find('a')['title'])
    except:
        break
