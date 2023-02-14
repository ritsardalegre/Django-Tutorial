from django.contrib import admin
from django.urls import path
from . import views # <------ importing views.py in the same folder



urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    # path("march", views.march),
    path('', views.challenges_list, name="index"), # /challenges
    path('<int:month>', views.monthly_challenge_num), #DYNAMIC PATHS SEGMENTS
    path('<str:month>', views.monthly_challenge, name="month_challenge"), #<------- <str:month> is a dynamic path segments that is
                                                                          # a string or converted to string
                                                                          # name = '' <-- constructing path pointing to url
    
]