import requests
from bs4 import BeautifulSoup as bs

username = 'captain_cuckoo' #imgflip account username
password = 'asdasdasd' #imgflip account password

search = 'https://imgflip.com/memesearch?q='

def SearchMeme(name):
	search = 'https://imgflip.com/memesearch?q='
	x = name.split()
	for i in range(len(x)):
		if i == 0:
			search = search + x[i]
		else:
			search = search + '+' + x[i]
	search = search + "&nsfw=on"
	page = requests.get(search) 
	
	soup = bs(page.content, 'html5lib')
	
	s = soup.findAll('a') 
	
	links = []
	
	for i in s:
		links.append(i['href'])
	
	
	ids = []
	
	for i in links:
		x = i.split('/')
		for i in range(0,len(x)):
			if x[i] == "memetemplate":
				ids.append(x[i+1])



	try:

		
		return ids[0]
	except:
		return "```template not found```"
	

#actually generates the meme using the imgflip api
def GenerateMeme(id,text):



	URL = 'https://api.imgflip.com/caption_image'
	params = {
	    'username':username,
	    'password':password,
	    'template_id':id
	}
	for i in range(0,len(text)):
		params["boxes["+str(i)+"][text]"] = text[i]
	if len(text) == 0:
		params["text0"] = ''
	response = requests.request('POST',URL,params=params).json()
	return response


#just create the meme with the imgflip api cant add more than 2 texts cause their api is shit
def GetMeme(name,text=[" "]):
	id = SearchMeme(name)
	link = GenerateMeme(id,text)
	return link

