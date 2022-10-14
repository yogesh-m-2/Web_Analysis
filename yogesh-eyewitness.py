import requests as r
import threading
import sys
import getopt
import os  

if(not os.path.exists("eyewitness/")):
	os.mkdir(("eyewitness/"))


global k_
k_ = {
    's_key': None,
    'threads': 1
}

def help(_exit_=False):
    print("Usage: %s [OPTION]\n" % sys.argv[0])
    print("\t-s\tSubdomains File Name")
    if _exit_:
        sys.exit()

header={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"}


top="""<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
  padding: 30px;
}
h1{
	padding: 35px;
}
</style>
<title> Yogesh Eyewitness</title>
<body>
<h1>Yogesh Eye Witness Report</h1>
<table style="width:100%">"""

bottom="""
</body>
</head>
</html>"""

domain_lines=""
pages = ""
def start_thread(page):
	global domain_lines,top,bottom,pages
	content=""
	indexpage=open("eyewitness/index"+str(page)+".html","w")
	for j in range((page*10),((page+1)*10)):
		try:
			url=domain_lines[j].strip("\n")
			res=r.get("http://"+url,headers=header,timeout=3)
			file=open("eyewitness/"+str(j)+".html","w")
			file.write(res.text)
			content=content+"""
<tr>
    <td><a href="""+url+""">"""+url+"""</a></td>
    <td><iframe width="500" height="500" src="./"""+str(j)+""".html"></iframe></td>
</tr>"""
		except Exception as e:
			continue
	print(pages)
	indexpage.write(top+content+pages+bottom)
	indexpage.close()

def submain(file):
	global domain_lines,pages
	domains=open(file)
	domain_lines=domains.readlines()
	length=len(domain_lines)
	divided=int(length/10)
	for j in range(0,divided):
		pages=pages+"""<a href="index"""+str(j)+""".html">-"""+str(j)+"""</a>"""
	for i in range(0,divided):
		sent="No"
		while(sent=="No"):
			if(threading.active_count()<10):
				ti = threading.Thread(target=start_thread, args=(i,))
				ti.start()
				sent="Yes"


def main():
	global k_
	if len(sys.argv) < 2:
		help(1)
	try:
		opts, args = getopt.getopt(sys.argv[1:],'s:l:p:o:t:T::u:kv',['s='])
	except Exception as e:
		print(e)
	for o, a in opts:
		if o == '-s':
			k_['s_key'] = a
		if o == '--help':
			help(1)
	submain(k_['s_key'])

if __name__ == '__main__':
	main()
