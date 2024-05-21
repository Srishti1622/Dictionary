from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def homePage(request):
    if request.method=='POST':
        keyword=request.POST.get('keyword')
        print(keyword)

        url=f"https://www.google.com/search?q={keyword}+meaning"
        resp=requests.get(url)
        soup=BeautifulSoup(resp.text,'lxml')
        print(soup.text)
        # print(soup.find_all('div',class_="vmod"))
        # print(soup.find_all('ol',class_="eQJLDd"))

        
    return render(request,'dict/home.html',{})
