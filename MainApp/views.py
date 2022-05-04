from django.shortcuts import render, redirect
from .forms import EntryForm, TopicForm
from MainApp.forms import TopicForm


from .models import Topic, Entry
# Create your views here.
#Homepage

def index(request):
    return render(request, 'MainApp/index.html') #must be consistent with naming on urls.py file
                                                    #render a page to the browser using the template
                                                    #folder inside templates folder must be same name as overarching folder


def topics(request):
    topics = Topic.objects.order_by('-date_added') #can't use topics.all, to make it descending order, add a mius sign in () #to get all topics: ".all()"

    context = {'topics': topics} #key = what you have to refer to it as in the HTML
                                 #value = what you called it in this file (on line 14)
    return render(request, 'MainApp/topics.html', context) #after the / is what the name of the file must be in the templates folder
                                        
def topic(request, topic_id): #loading individual topics onto the website (ex: chess and rock climbing)
    topic = Topic.objects.get(id= topic_id) #topic (singular) = topic in the overall topics page. Capital T Topic = object from models.py file 
    entries = topic.entry_set.all() #object

    context = {'topic' : topic, 'entries' :entries} #object, dictionary, passes information from the view to use in the template

    return render(request, 'MainApp/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
            
        if form.is_valid(): #this validates if something on the form is specified as required and if it's on the form
            new_topic = form.save() #will directly save this to the database

            return redirect('MainApp:topics')

    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)


def new_entry(request,topic_id): #need topic_id so it knows which topic to link the new entry to
                                #topic_id in () = 1,2,3... int object
    topic = Topic.objects.get(id=topic_id) #this is the topic OBJECT 
    #load entry based on post or get request
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False) #form will only store: topic, text, & date added (automatic)
                                                #commit=False --> saves new entry object ready to write to DB, but doesn't actually save to DB yet
                                                #need to assign topic attribute before adding to DB
            new_entry.topic =  topic #line 47 is how we're getting the topic_id. assigning the topic to new_entry object
            new_entry.save()
            return redirect('MainApp:topic', topic_id=topic_id) #topic_id = defined in url file, 2nd topic_id = defined in line 47 (not the object, the int #?)

    context = {'form':form, 'topic':topic}
    return render(request, 'MainApp/new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic #how to get the associated topic on the entry we're editing. lower case b/c referring to the variable

    if request.method !='POST':
        form = EntryForm(instance=entry) #need the specific entry instance, not a new entry. instance = entry object in line 68.
    else:
        form = EntryForm(instance=entry, data=request.POST) #post request = saving. want to save it to same entry, so instance = entry
        if form.is_valid():
            form.save()
            return redirect('MainApp:topic', topic_id=topic.id) 

    context = {'form':form, 'topic':topic, 'entry':entry}
    return render(request, 'MainApp/edit_entry.html', context)
