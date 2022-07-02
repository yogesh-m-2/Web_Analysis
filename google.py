import re
import requests as r
import sys 
import getopt

global k_

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
    print("\t-search\tsearch string")
    print("\t-from\tfrom page number to search results")
    print("\t-t\ttill the page number to search results")
    if _exit_:
        sys.exit()

header={"User-Agent": "Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"}

def main():
	if len(sys.argv) < 2:
		help(1)
	try:
		opts, args = getopt.getopt(sys.argv[1:],'d:l:p:o:t:T::u:kv',['search=', 'from=', 'to=', 'v', 'pages=', 't=', 'T=', 'u=', 'k'])
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
	if(k_['page_start'] and k_['page_end']):
		for i in range(k_['page_start'],k_['page_end']+1):
			page=str((i-1)*10)
			print(page)
			url="""https://www.google.com/search?q="""+k_['s_key']+"""&hl=en&sxsrf=ALiCzsbt1g0F0ScjUkcJTW6tg17KX9hg_A:1656692975843&ei=7yC_YuCHM-SZseMPsreUoAY&start="""+page+"""&sa=N&ved=2ahUKEwigu86ijtj4AhXkTGwGHbIbBWQQ8tMDegQIGBA6&biw=2400&bih=1217&dpr=0.8"""
			res=r.get(url,headers=header)
			res=str(res.text)
			x = re.compile('href="/url\?q=https://([^\/]*)')
			ips=x.findall(res)
			for ip in ips:
				print(ip)
	if(k_['pages']):
		for i in range(1,k_['pages']+1):
			page=str((i-1)*10)
			url="""https://www.google.com/search?q="""+k_['s_key']+"""&hl=en&sxsrf=ALiCzsbt1g0F0ScjUkcJTW6tg17KX9hg_A:1656692975843&ei=7yC_YuCHM-SZseMPsreUoAY&start="""+page+"""&sa=N&ved=2ahUKEwigu86ijtj4AhXkTGwGHbIbBWQQ8tMDegQIGBA6&biw=2400&bih=1217&dpr=0.8"""
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
