import requests, re, urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
fileContent = []
filename = "WebPath.txt"
fyle = open(filename).read().splitlines()
for line in fyle:
    fileContent.append(line)

#print((fileContent))

urlcnt = 0;
urls = ["https://www.secdaemons.org/"]
url = "https://www.secdaemons.org/"

while urlcnt < len(fileContent):
    urls.append( url + fileContent[urlcnt])
    urlcnt += 1

#print(urls)
checking = 0

while checking < len(urls):
    
    
    check = requests.get(urls[checking], verify = False)
    #print('here1')
    if check.status_code == 200:
        #print('here2')
        content = check.content
        #print(content)
        regexPhone = '\(\d{3}\)\s\d{3}\-\d{4}'
        #regexPhone = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
        #regexEmail = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,4}'
        regexEmail = '\w+\@\w+\.\w{3}'
        matchPhone = re.findall(regexPhone,content)
        matchEmail = re.findall(regexEmail,content)
        #print(matchPhone)
        #print(matchEmail)
        if matchPhone:
            print('V   Website URL where phone number(s) were found   V')
            print(urls[checking])
            print('Phone Number Incoming!')
            print(matchPhone)
            checking += 1
        elif matchEmail:
            print('V   Website URL where email address(es) were found   V')
            print(urls[checking])
            print('Email incoming!')
            print(matchEmail)
            checking += 1
    else:
        checking += 1
            
