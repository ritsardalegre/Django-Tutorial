from django.shortcuts import render

# Create your views here.
from django.http import Http404,HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse #importing reverse() for redirecting
from django.template.loader import render_to_string #import templates as string


monthly_challenges = {
    'january': "Swim for 30min!",
    'february': "Swim for 30min!",
    'march': "Swim for 30min!",
    'april': "Swim for 30min!",
    'may': "Swim for 30min!",
    'june': "Swim for 30min!",
    'july': "Swim for 30min!",
    'august': "Swim for 30min!",
    'september': "Swim for 30min!",
    'october': "Swim for 30min!",
    'november': "Swim for 30min!",
    'december': None,
}

# def january(request):
#     return HttpResponse('Swim for 30min!')

# def february(request):
#     return HttpResponse('Walk for at least 20 minutes everyday!')

# def march(request):
#     return HttpResponse("Learn Django for 40min")


def challenges_list(request):
    list_items = " "
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    month_path = reverse("month_challenge", args=[months])
    #     list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    # response_data = f" <ul> {list_items} </ul>"
    # return HttpResponse(response_data)

    return render(request, "challenges/index.html", {
        "month_list" : months,
        "month_path" : month_path
    })

def monthly_challenge_num(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse("month_challenge", args=[redirect_month]) #redirecting or creating a string path /challenges/month

        return HttpResponseRedirect(redirect_path)
    except:       
        # returning 404 option 1
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

        raise Http404()


def monthly_challenge(request, month):

    # challenge_text = None
    # if month in monthly_challenges:
    #     challenge_text = monthly_challenges[month]
    # else:
    #     return HttpResponseNotFound("This month is not supported!")
    # return HttpResponse(challenge_text)

    # OR this code

    try:
        challenge_text = monthly_challenges[month]
        # month.capitalize()
        # challenge_text = monthly_challenges.keys()

        # option 1
        # to render html template:

        # response_data = render_to_string("challenges/challenge.html") 
        # return HttpResponse(response_data)

        # option 2
        # to render html template  is using render()
        return render(request,'challenges/challenge.html', 
            {
              "text": challenge_text,
              "month": month
              
              }) #render(request, template/folder, dictionary to be used in the template)
    except:
        # returning 404 option 1
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

        raise Http404() #django will find 404.html in the roots folder that's why you should name the file 404.html
