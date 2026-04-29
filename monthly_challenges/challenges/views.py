from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


challenges = [
        {'month': 'january', 'challenge': "let's go to work"},
        {'month': 'feburary', 'challenge': "do swim"},
        {'month': 'march', 'challenge': "let's practice django every day"},
        {'month': 'april', 'challenge': "none"},
        {'month': 'may', 'challenge': "around the mountain"},
        {'month': 'june', 'challenge': "draw something"},
        {'month': 'july', 'challenge': "no vacation"},
        {'month': 'august', 'challenge': "fix air conditioner"},
        {'month': 'september', 'challenge': "buy an ubrella"},
        {'month': 'october', 'challenge': "meet someone"},
        {'month': 'november', 'challenge': "last dance for running"},
        {'month': 'december', 'challenge': "merry christmas"},
    ]
'''
def index(request):
    link = "<ul>"
    for m in challenges:
        link += f'<li><a href="{reverse("month-challenge", args=[m['month']])}">{m["month"]}</a></li>'
    print(link)
    link += "</ul>"
    return HttpResponse(link)
'''

def index(request):
    re_path = reverse("month-challenge", args=["january"])               
    return render(request, "challenges/index.html", {'challenges': challenges, 'path': re_path[:-7]})


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
    try:
        t_month = list(filter(lambda i : i['month'] == month or i['month'][0:3] == month, challenges))[0]    
        context = {
            'month': t_month['month'],
            'ch': t_month['challenge']}    
        return render(request, "challenges/challenges.html", context)       
    except:
        return HttpResponseNotFound("that's not a month")