# William Go
# CS 4250
# Assignment 4

import urllib as urllib
import bs4 as bs
from pymongo import MongoClient

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

#The frontier object?   
class Frontier: 
    def __init__(self, starting_url):
        self.queue = [starting_url]
        self.visited = set()

#The actual crawler based on pseudocode
def crawlerThread(frontier):


def main(): 
    starting_url = 'https://www.cpp.edu/sci/computer-science/'
    frontier = Frontier(starting_url)
    crawlerThread(frontier)

if __name__ == "__main__":
    main()