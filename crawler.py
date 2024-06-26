# William Go
# CS 4250
# Assignment 4

import urllib as urllib
import bs4 as bs
from pymongo import MongoClient

#Connect the Database
def connectDataBase():
    DB_NAME = "CPP"
    DB_HOST = "localhost"
    DB_PORT = "27017"
    try:
        client = MongoClient(host=DB_HOST, port=DB_PORT)
        db = client[DB_NAME]
        return db
    except:
        print("Database not connected successfully")

#Pseudocode
# procedure crawlerThread (frontier)
#      while not frontier.done() do
#           url <— frontier.nextURL()
#           html <— retrieveHTML(url)
#           storePage(url, html)
#           if target_page (html)
#                clear_frontier()
#           else
#                for each not visited url in parse (html) do
#                     frontier.addURL(url)
#                end for
#      end while
# end procedure

#The frontier object 
class Frontier: 
    def __init__(self, starting_url):
        self.queue = [starting_url]
        self.visited = set()

    #Add urls to queue if not yet visited
    def addURL(self, url):
        if url not in self.visited and url not in self.queue:
            self.queue.append(url)

    #Next URL in queue (pop the previous)
    def nextURL(self):
        url = self.queue.pop(0)
        self.visited.add(url)
        return url

    #Done if the queue is 0
    def done(self):
        return len(self.queue) == 0

#If it is a page, store the page in the db
def storePage(url, html, db):
    page = {"url": url, "html": html}
    professors.insert_one(page)

#Getting the HTML
def getHTML(url):
    openURL = urllib.request.urlopen(url)
    html = openURL.read()
    return html

def findLink(html):
    links = html.find_all('a', href=True)
    linksList = []
    for link in links:
        url = link['href']
        linksList.append(url)
    return linksList

#Function to check if it is the actual target
def target(html):
    headings = html.find_all('h2')
    #Check for heading
    for heading in headings:
        if heading.get_text().strip() == 'Permanent Faculty':
            return True
    return False

#The actual crawler based on pseudocode
def crawlerThread(frontier):
    while not frontier.done():
        url = frontier.nextURL()
        #Check if what is grabbed is a url
        if url is not None:
            html = getHTML(html)
            storePage(url, html)
            if target(html):
                frontier.queue.clear()
            else:
                links = findLink(html)
                for link in links:
                    frontier.addURL(link)

def main(): 
    starting_url = 'https://www.cpp.edu/sci/computer-science/'
    db = connectDataBase()
    professors = db.professors
    frontier = Frontier(starting_url)
    crawlerThread(frontier)

if __name__ == "__main__":
    main()