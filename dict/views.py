from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests

# Create your views here.
def homePage(request):

    
    if request.method=='POST':
        keyword=request.POST.get('keyword')
        print(keyword)

        response = requests.get('https://www.dictionary.com/browse/'+keyword)
        response2 = requests.get('https://www.thesaurus.com/browse/'+keyword)

        if response:
            soup_1 = BeautifulSoup(response.text, 'lxml')
            # print(soup_1)
            meaning = soup_1.find_all('ol', {'class': 'lpwbZIOD86qFKLHJ2ZfQ E53FcpmOYsLLXxtj5omt'})
            meaning_1 = meaning[0].getText()
        else:
            word = f"Sorry we couldn't find your word {word} in our records."
            meaning = ''
            meaning_1 = ''

        if response2:
            soup_2 = BeautifulSoup(response2.text, 'lxml')

            synonyms = soup_2.find_all('a', {'class': 'css-1kg1yv8 eh475bn0'})
            synonym_list = []
            for b in synonyms[0:]:
                re = b.text.strip()
                synonym_list.append(re)
            main_synonym_list = synonym_list

            antonyms = soup_2.find_all('a', {'class': 'css-15bafsg eh475bn0'})
            antonyms_list = []
            for c in antonyms[0:]:
                r = c.text.strip()
                antonyms_list.append(r)
            main_antonym_list = antonyms_list
        else:
            main_synonym_list = ''
            main_antonym_list = ''


        results = {
            'word' : keyword,
            'meaning' : meaning_1,
        }

        print(results,main_synonym_list,main_antonym_list)

        return render(request,'dict/home.html',{'results':results})

    return render(request,'dict/home.html',{})

