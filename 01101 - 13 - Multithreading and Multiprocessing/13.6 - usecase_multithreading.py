'''
Real-World Scenario: Multithreading for IO Bound Tasks
Scenario: Web Scraping
Web Scraping often involves making numerous network requests to fetch web pages.
These tasks are I/O bound because they spend a lot of time waiting for responses from server.
Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently.
'''

'''
https://python.langchain.com/v0.2/docs/introduction/
https://python.langchain.com/v0.2/docs/tutorials/
https://python.langchain.com/v0.2/docs/concepts/
'''
import threading 
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/tutorials/',
    'https://python.langchain.com/v0.2/docs/concepts/',
]

def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_contents, args=(url,))
    threads.append(thread)
    thread.start() ## Till we get the entire response, it will go back to the next thread

for thread in threads:
    thread.join()

print("All web pages fetched")

    
    
