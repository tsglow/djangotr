from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


challenges = [
        {'month': 'january', 'challenge': "let's go to work"},
        {'month': 'feburary', 'challenge': "do swim"},
        {'month': 'march', 'challenge': "let's practice django every day"},
        {'month': 'april', 'challenge': "go to cycle"},
        {'month': 'may', 'challenge': "around the mountain"},
        {'month': 'june', 'challenge': "draw something"},
        {'month': 'july', 'challenge': "no vacation"},
        {'month': 'august', 'challenge': "fix air conditioner"},
        {'month': 'september', 'challenge': "buy an ubrella"},
        {'month': 'october', 'challenge': "meet someone"},
        {'month': 'november', 'challenge': "last dance for running"},
        {'month': 'december', 'challenge': "merry christmas"},
    ]

def index(request):
    link = "<ul>"
    for m in challenges:
        link += f'<li><a href="{reverse("month-challenge", args=[m['month']])}">{m["month"]}</a></li>'
    print(link)
    link += "</ul>"
    return HttpResponse(link)


def num_redirect(request, month):        
    try: 
        forward_month = challenges[month - 1]['month'] 
        print(forward_month)
        re_path = reverse("month-challenge", args=[forward_month])
        print(re_path)
        return HttpResponseRedirect(re_path)
    except:
        return HttpResponseNotFound("that's not a month")


def mon_challenge(request, month):    
    #try: 
    res = list(filter(lambda i : i['month'] == month, challenges))[0]['challenge']
    # response_data = f"<h1>{res}</h1>"
    response_data = render_to_string("challenges/challenges.html")
    return HttpResponse(response_data)
    #except:
        #return HttpResponseNotFound("<h1>that's not a month</h1>")
    
        