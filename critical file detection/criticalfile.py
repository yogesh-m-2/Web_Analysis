import threading
import requests

f=open("dicc.txt","r")

for i in f:
    
    print(i.read())















x = requests.get('https://w3schools.com')
print(x.status_code)

