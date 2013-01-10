# 
# Use Requests to make the crawling of information from the websites.
#
import requests

class Crawler:

    def __init__(self):
        self.url = 'http://www.carris.com.br'
        self.url_eptc = 'http://www.eptc.com.br/EPTC_Itinerarios/Linha.asp?cdEmp=3'

    def get_url(self, url):
        r = requests.get(self.url)
        if r.status_code() == requests.codes.ok:
            print r.json()
        else:
            print "check the url"
