from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges_to = {
    "january": "Complete a 30-day fitness challenge.",
    "february": "Read one book on personal development.",
    "march": "Start a new hobby and practice it daily.",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Write a daily journal entry.",
    "august": "Meditate for 10 minutes every day.",
    "september": "Declutter and organize one area of your home.",
    "october": "Try a new recipe every week.",
    "november": "Volunteer for a local charity or cause.",
    "december": "Reflect on your year and set goals for the next year."
}


def index(request):
    list_items = ""
    months = list(monthly_challenges_to.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<h3><li><a href=\"{month_path}\">{capitalized_month}</a></li></h3>"
    
    Response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(Response_data)

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_to.keys())
    if month >len(months):
        return HttpResponseNotFound("this does not exists")
    
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_to[month]
        response_to_send = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_to_send)
    except:
        return HttpResponseNotFound("This is not found broooooooo")

