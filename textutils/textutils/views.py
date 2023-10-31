
## ================================
# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse(''' Harry Django CodeWithHarry ''')
#
# def about(request):
#     return HttpResponse(''' About Harry Bhai ''')

### =============================================
# from django.http import HttpResponse
# from django.shortcuts import render
#
# def index(request):
#     # return HttpResponse(" HOME ")
#     return render(request, 'index.html')
#
# def removepunc(request):
#     djtext= request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse(" remove punc ")
#     # return render(request, 'index.html')
#
# def capfirst(request):
#     return HttpResponse(" Capitalize First ")
#
# def newlineremove(request):
#     return HttpResponse(" Newline Remove")
#
# def spaceremove(request):
#     return HttpResponse(" Space Remover ")
#
# def charcount(request):
#     return HttpResponse(" Char Count")
#

### ========================================

# # I have created this file - Harry
# from django.http import HttpResponse
# from django.shortcuts import render
#
#
# def index(request):
#     return render(request, 'index.html')
#
#     # return HttpResponse("Home")
#
#
#
# def analyze(request):
#     #Get the text
#     djtext = request.GET.get('text', 'default')
#
#     # Check checkbox values
#     removepunc = request.GET.get('removepunc', 'off')
#     fullcaps = request.GET.get('fullcaps', 'off')
#     newlineremover = request.GET.get('newlineremover', 'off')
#     extraspaceremover = request.GET.get('extraspaceremover', 'off')
#
#     #Check which checkbox is on
#     if removepunc == "on":
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analyzed = ""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#         params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#     elif fullcaps == "on":
#         analyzed = ""
#         for char in djtext:
#             analyzed = analyzed + char.upper()
#         params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
#
#     elif newlineremover == "on":
#         analyzed = ""
#         for char in djtext:
#             if char != "\n":
#                 analyzed = analyzed + char
#         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
#
#         # Analyze the text
#
#         return render(request, 'analyze.html', params)
#
#     elif (extraspaceremover == "on"):
#         analyzed = ""
#         for index, char in enumerate(djtext):
#             if not (djtext[index] == " " and djtext[index + 1] == " "):
#                 analyzed = analyzed + char
#
#         params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
#
#         # Analyze the text
#         return render(request, 'analyze.html', params)
#
#     else:
#         return HttpResponse("Error")
#
# # def capfirst(request):
#
# #     return HttpResponse("capitalize first")
# #
# # def newlineremove(request):
# #     return HttpResponse("newline remove first")
# #
# #
# # def spaceremove(request):
# #     return HttpResponse("space remover back")
# #
# # def charcount(request):
# #     return HttpResponse("charcount ")
#
#### ==================================

# from django.http import HttpResponse
# from django.shortcuts import render
#
#
# def index(request):
#     return render(request, 'index.html')
#
#     # return HttpResponse("Home")
#
#
# def ex1(request):
#     sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
#              '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
#              '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
#              '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
#
#              '''<h2>Google page</h2>
#              <a href= "https://www.google.com"> Google </a><br>
#              <a href= "https://www.youtebe.com"> YouTube </a><br>
#              <a href= "https://www.instagram.com"> Inatagram </a>
#              '''
#
#              ]
#     return HttpResponse((sites))

###===================================

# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def ex1(request):
    sites = ['''<h1>For Entertainment  </h1> <a href="https://www.youtube.com/"> Youtube Videos</a> ''',
             '''<h1>For Interaction  </h1> <a href="https://www.facebook.com/"> Facebook</a> ''',
             '''<h1>For Insight  </h1> <a href="https://www.ted.com/talks"> Ted Talks</a> ''',
             '''<h1>For Internship  </h1> <a href="https://www.internshala.com">Internship</a> ''']
    return HttpResponse((sites))

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")




