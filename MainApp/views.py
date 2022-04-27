from django.shortcuts import render

from .models import Topic
# Create your views here.
#Homepage

def index(request):
    return render(request, 'MainApp/index.html') #must be consistent with naming on urls.py file
                                                    #render a page to the browser using the template
                                                    #folder inside templates folder must be same name as overarching folder


def topics(request):
    topics = Topic.objects.all() #can't use topics.all, to make it descending order, add a mius sign in ()

    context = {'topics': topics} #key = what you have to refer to it as in the HTML
                                 #value = what you called it in this file (on line 14)
    return render(request, 'MainApp/topics.html', context) #after the / is what the name of the file must be in the templates folder
                                        