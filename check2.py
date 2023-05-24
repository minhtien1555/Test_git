import requests
import urllib3


Session=requests.Session()

for i in range (100000000000,200000000000):

#the required first parameter of the 'get' method is the 'url':
    x = Session.head(f'http://localhost:8080/login/{str(i).rjust(12, "0")}')
    #print the response text (the content of the requested file):
    if (x.status_code==200):
        print(i)
        break
    print(x.status_code, i)