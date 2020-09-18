from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")
def count(request):
    Writtentext = request.GET["Writtentext"]
    count_word = Writtentext.split()  #truning words into list and count them
    return render(request, "count.html", {"Writtentext":Writtentext, "count_word1": len(count_word)})#len is for counting of words
def about_learning (request):
    return render(request, "about.html")
