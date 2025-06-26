from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
# from django.template.loader import render_to_string

# Create your views here.

# def january(request):
#     return HttpResponse("<h1>January</h1>")

# def february(request):
#     return HttpResponse("<h1>February</h1>")

monthly_challenge = {
    'january' : 'Eat no meat for the next month',
    'february' : 'Walk for at least 20 minutes every day',
    'march' : 'Learn Django for at least 20 minutes every day',
    'april' : 'Eat no meat for the next month',
    'may' : 'Walk for at least 20 minutes every day',
    'june' : 'Learn Django for at least 20 minutes every day',
    'july' : 'Eat no meat for the next month',
    'august' : 'Walk for at least 20 minutes every day',
    'september' : 'Learn Django for at least 20 minutes every day',
    'october' : 'Eat no meat for the next month',
    'november' : 'Walk for at least 20 minutes every day',
    'december' : None
}

def monthly_challenges_by_number(request, month):
    try:
        forward_month = list(monthly_challenge.keys())
        months = forward_month[month - 1]
        redirected_path = reverse("month-challenge", args=[months])
        return HttpResponseRedirect(redirected_path)
    except:
        raise Http404()
    
    
def monthly_challenges(request, month):
    try:
        challenges_text = monthly_challenge[month]
        return render(request, "challenges/index.html", {
            'text' : challenges_text,
            'month' : month
        })
    except:
        raise Http404()
    

def home(request):
    
    months = list(monthly_challenge.keys())
    return render(request, 'challenges/home.html', {
        "months" : months,
    })
    
    # for month in months:
    #     cap_month = month.capitalize()
    #     month_path = reverse("month-challenge", args = [month])
    #     item_list += f'<li><a href = "{month_path}">{cap_month}</a></li>'
    
    # response_data = f"<ul>{item_list}</ul>"
    
    # return HttpResponse(response_data)