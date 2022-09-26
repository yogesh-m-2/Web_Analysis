import mechanize
from bs4 import BeautifulSoup
import re
import re
import requests as r
import sys 
import getopt

global k_

def get_url(skey,page):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0')] 
    br.open('http://www.google.com/')   

    # do the query
    br.select_form(name='f')   
    br.form['q'] = 'scrapy' # query
    data = br.submit()
    url=data.geturl()
    return url.replace("scrapy",skey+"&start="+page)


k_ = {
    's_key': None,
    'threads': 1,
    'page_start': None,
    'page_end': None,
    'pages': None,
    'timeout': None
}
def help(_exit_=False):
    print("Usage: %s [OPTION]\n" % sys.argv[0])
    print("\t--search\tsearch string")
    print("\t--from\tfrom page number to search results")
    print("\t--to\ttill the page number to search results")
    print("\t--pages\tNumber of pages to get results of")
    if _exit_:
        sys.exit()

header={"User-Agent": "Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"}

def main():
	if len(sys.argv) < 2:
		help(1)
	try:
		opts, args = getopt.getopt(sys.argv[1:],'d:l:p:o:t:T::u:kv',['search=', 'from=', 'to=', 'help', 'pages=', 't=', 'T=', 'u=', 'k'])
	except Exception as e:
		print(e)

	for o, a in opts:
		if o == '--search':
			k_['s_key'] = a
		if o == '--from':
			k_['page_start'] = int(a)
		if o == '--to':
			k_['page_end'] = int(a)
		if o == '--pages':
			k_['pages'] = int(a)
		if o == '--help':
			help(1)
	if(k_['page_start'] and k_['page_end']):
		for i in range(k_['page_start'],k_['page_end']+1):
			page=str((i-1)*10)
			print(page)
			url=get_url(k_['s_key'],page)
			res=r.get(url,headers=header)
			res=str(res.text)
			x = re.compile('href="/url\?q=https://([^\/]*)')
			ips=x.findall(res)
			for ip in ips:
				print(ip)
	if(k_['pages']):
		for i in range(1,k_['pages']+1):
			page=str((i-1)*10)
			url=get_url(k_['s_key'],page)
			res=r.get(url,headers=header)
			res=str(res.text)
			x = re.compile('href="/url\?q=https://([^\/]*)')
			ips=x.findall(res)
			for ip in ips:
				print(ip)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt) as e:
        sys.exit(0)
