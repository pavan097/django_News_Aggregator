from django.shortcuts import render, redirect
import bs4
import requests
from .models import NewsData
from django.http import HttpResponse


def web_scrap(request):
    # s = requests.Session()
    # s.headers = {
    #     "User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"
    # }

    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = 'https://www.theonion.com/'

    # content = s.get(url, verify=False).content

    content = requests.get(url, verify=False).content

    soup = bs4.BeautifulSoup(content, "html.parser")
    News = soup.find_all('div', {"class":"curation-module__item"})
    print('news data :',News)

    for i in News:
        main = i.find_all('a')[0]
        print('main data :',main)
        link = main['href']
        image_src = str(main.find('img')['srcset']).split(" ")[-4]
        title = main['title']
        a = NewsData()
        a.title = title
        a.url = link
        a.img = image_src
        a.save()

    return HttpResponse('success')


def newsList(request):
    data = NewsData.objects.all()
    return render(request, 'home.html', {'data':data})