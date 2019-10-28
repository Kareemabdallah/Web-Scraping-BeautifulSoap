import bs4
import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup

# Passing UserAgent Verification in case of HTTP 403 forbidden errors
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

def return_request():
		
	# Url declaration
	reg_url = 'http://www.metacritic.com/game/playstation-4'
	
	# Opens up connection and grab headers
	req = Request(url=reg_url, headers=headers)
	#print (req)
	#print (type(req))
	#return_request(req)

def return_html(req):

	# Offloads content into a variable
	page_html = urlopen(req).read()

	# Test the url content
	print(page_html)
	# Calling soup function to parse HTML file
	page_soup = soup(page_html, "html.parser")
	return return_html(req)
	#print ("page_soup")
	#print (page_soup)
	#print ("------------------------")
	#print ("------------------------")
	#print ("------------------------")

def find_html(titles,scores):
	titles = page_soup.findAll("td",{"class":"clamp-summary-wrap"})
	scores = page_soup.findAll("div",{"class":"clamp-score-wrap"})
	result = []

	return find_html(titles, scores)

#titles, scores = return_html(req())

def return_json(titles, scores):


	for title, score in zip(titles, scores):

		data = {
			"title": title.h3.text.strip(),
			"score": score.a.text.strip()
		}

		result.append(data)

	print(json.dumps(result, indent=2))

	return json.dumps(result, indent=2)

 #print("title: " + game)
# Search for the game by title
#titles = page_soup.findAll("td",{"class":"clamp-summary-wrap"})
#print (type(title))
# Move one item in title for testing
#title = titles[0]
# check number of games in title
#title = title.contents[0].h3.text.strip()
#title = titles.contents[1].h3
#title = title.findChildren("h3")
#t = title[0]

#t.a

# Search for score


# Test with one item
#score = scores[0]

# get score
#print ("scores")
#print (score)
#print ("------------------------")
#print ("------------------------")
#print ("------------------------")

#'\n89\n'.replace("backslash n", "") -> 89

#gns = page_soup.findAll("td",{"class":"clamp-summary-wrap"})

#gn.scores[1].h3.get_text()

#gn.findAll("a", {"class":"title"})

# Find the game by title
#title = page_soup.findAll("span",{"class":"title"})
#for cont in gns:
#...     cont.contents[1].h3.get_text()
#...     cont.contents[1].a.get_text()