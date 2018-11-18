
from django.shortcuts import render

def home(request) :
    return render(request, 'home.html')

def count(request) :
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()

    wordDictionary = {}

    for word in wordlist:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    return render(
    request, 'count.html',
    {'text': fulltext,
    'textCount': len(wordlist),
    'kamusKata': wordDictionary.items()})