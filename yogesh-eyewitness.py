import requests as r
import threading
# import os

# efolder="eyewitness"
# path = os.path.join(".", efolder)
# os.mkdir(path)


header={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"}

# import requests 
# from bs4 import BeautifulSoup
  

# web_url = "www.geeksforgeeks.org"
# file1 = open("eyewitness/"+web_url+".html", "w")

# html = requests.get("http://"+web_url).content
# file1.write(str(html))
# file1.close()

# indexpage=open("eyewitness/index.html", "w")

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
# indexpage.write(content)
# indexpage.close()

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

def main():
	global domain_lines,pages
	domains=open("subdomains")
	domain_lines=domains.readlines()
	length=len(domain_lines)
	divided=int(length/10)
	for j in range(0,divided):
		pages=pages+"""<a href="index"""+str(j)+""".html">-"""+str(j)+"""</a>"""
	for i in range(0,divided):
		ti = threading.Thread(target=start_thread, args=(i,))
		ti.start()
	



		


if __name__ == '__main__':
	main()


# soup = BeautifulSoup(html, "html.parser")
  
# js_files = []
# cs_files = []
  
# for script in soup.find_all("script"):
#     if script.attrs.get("src"):
          
#         # if the tag has the attribute 
#         # 'src'
#         url = script.attrs.get("src")
#         js_files.append(url)
  
  
# for css in soup.find_all("link"):
#     if css.attrs.get("href"):
          
#         # if the link tag has the 'href' 
#         # attribute
#         _url = css.attrs.get("href")
#         cs_files.append(_url)
  
# for i in js_files:
# 	try:
# 		route=""
# 		string=str(i).split("/")
# 		if(string[2]==web_url):
# 			for j in string:
# 				if(j!="https:" and j!=web_url and j!=""):
# 					route=route+j+"/"
# 					os.mkdir(route)
# 			os.remove(route)


# 	except:
# 		continue
	
# print(f"Total {len(cs_files)} CSS files found")