import requests
from bs4 import BeautifulSoup as bs #Renaming

github_user = input("Input GitHub user: ")
url = 'https://github.com/'+github_user
r = requests.get(url) #From the imported library
soup = bs(r.content, 'html.parser') #Gives us the content response
profile_image = soup.find('img', {'alt' : 'avatar'})['src'] #Only retrieve the src attributes
print(profile_image)