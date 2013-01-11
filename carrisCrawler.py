import requests
from BeautifulSoup import BeautifulSoup

# EPTC data url: http://www.eptc.com.br/EPTC_Itinerarios/
# query: 'http://www.eptc.com.br/EPTC_Itinerarios/Cadastro.asp?Linha=' + %s + '&Tipo=I&Veiculo=1&Sentido=0&Logradouro=0&Action=Itiner%E1rio'
# sample: http://www.eptc.com.br/EPTC_Itinerarios/Cadastro.asp?Linha=109-0&Tipo=I&Veiculo=1&Sentido=0&Logradouro=0&Action=Itiner%E1rio


class Crawler:
    def __init__(self, url):
        self.url = url
    def get_url(self):
        r = requests.get(self.url)
        if r.status_code == requests.codes.ok:
            return r.text
        else:
            print "check the url"

def query_eptc_url(q_value):
    id = q_value
    query = 'http://www.eptc.com.br/EPTC_Itinerarios/Cadastro.asp?Linha='+id+'&Tipo=I&Veiculo=1&Sentido=0&Logradouro=0&Action=Itiner%E1rio'
    return query

req = Crawler('http://www.eptc.com.br/EPTC_Itinerarios/Linha.asp?cdEmp=3')
html = req.get_url()
#print html
s = BeautifulSoup(html)
l = s.findAll('option')

# create and put contents in query list
q_list = []

for q in l:
    q_list.append(q['value'])

# crawl over the list and return the divs

for q in q_list:
    r_query = Crawler(query_eptc_url(q))
    h_query = r_query.get_url()
    s_query = BeautifulSoup(h_query)
    l_query = s_query.findAll(lambda tag: len(tag.name) == 1)
    for l in l_query:
        print l
