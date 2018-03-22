from urllib.parse import urljoin
import os
from os import path, getcwd
import bs4
import requests
from requests import get
import sys

base_dir = 'C:\\Users\\greenleaf\\Desktop\\ThaiDL'
base_url = 'http://readingthai.wisc.edu/'
res = requests.get('http://readingthai.wisc.edu/thai-reader-site-volume-1.html')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.findAll('area')

pdflist=[]
for i in links:
    pdf = i['href']
    pdflist.append(pdf)

pdflink = []
filetype = 'pdf'
for npdf in pdflist:
    if filetype in npdf:
        pdflink.append(npdf)

for x in range(72):
    dllink = urljoin(base_url, pdflink[x])
    content = get(dllink, stream=True)
    if content.status_code == 200 and content.headers['content-type'] == 'application/pdf':
        with open(os.path.join(base_dir, pdflink[x][8:]), 'wb') as pdf:
            pdf.write(content.content)
            pdf.close()

