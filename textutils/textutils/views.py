# I have created this file - Udoy

from django.http import HttpResponse
from django.shortcuts import render

#       video-6
# def index(request):
#     return HttpResponse('<a href="https://www.facebook.com"> facebook </a>')

# def about(request):
#     return HttpResponse('about Udoy bhai')

# def hello(request):
#     return HttpResponse('<h1>Hello Udoy</h1>')

#       video-7-8

# def index(request):
#     # return HttpResponse("Home")
#     # params = {'name':'udoy', 'place':'mars'}
#     #       Get the text
#     print(request.GET.get('text', 'default'))
#     return render(request, 'index.html')


# def removepunc(request):
#     #       Analyze the text
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newlineremove")

# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'> back </a>")

# def charcount(request):
#     return HttpResponse("charcount")

#       video-10

def index(request):
    # user index2.html file there
    return render(request, 'index.html')


def analyze(request):
    #       Get the text
    # djtext = request.GET.get('text', 'default')
    djtext = request.POST.get('text', 'default')
    print(djtext)

    #       Check Checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')


    if removepunc == 'on':
        # return HttpResponse('Remove punc')
        # analyzed = djtext
        punctuations = '''!()-{}[];;'"\,<>/?@#^&$_'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'remove punction', 'analyze_text':analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose':'Changed to UpperCase', 'analyze_text':analyzed}
        return render(request, 'analyze.html', params)

    elif(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !='\n' and char !="\r":
                analyzed = analyzed + char

        params = {'purpose':'Remove New Lines', 'analyze_text':analyzed}
        return render(request, 'analyze.html', params)

    elif(spaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose':'Remove Extra Space', 'analyze_text':analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")