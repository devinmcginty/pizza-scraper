#	make sure you install requests & beautiful soup 4 to run this
import requests
from bs4 import BeautifulSoup
from random import choice
import webbrowser

def pizza_scrape(url):
	yelp = requests.get(url)
	#	check validity of given url
	if yelp.status_code != 200:
		#	this is bad dumb coding. Don't do this.
		raise Exception
	else:
		pizza = []
		#	full html content
		html = BeautifulSoup(yelp.content)
		links = html.findAll(name = 'a')
		for a in links:
			if a.string != None \
			and a.get('href') \
			and '/biz/' in a.get('href'):
				#	list of pizza places from given selection
				pizza.append(a.get('href'))
		#	gets random pizzeria
		pizzaUrl = 'http://www.yelp.com' + choice(pizza)
		print pizzaUrl
		webbrowser.open(pizzaUrl)

if __name__ == '__main__':
	yelp = 'http://www.yelp.com/search?cflt=pizza&find_loc=Philadelphia%2C+PA&attrs=RestaurantsDelivery'
	pizza_scrape(yelp)