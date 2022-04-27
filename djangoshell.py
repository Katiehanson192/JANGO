import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import *

topics = Topic.objects.all()

for t in topics:
    print(t.id, ' ',t) #going through all topics (chess and rockclimbing) and print the ID

t = Topic.objects.get(id=1) #.get = for specific object

print(t.text)
print(t.date_added)

entries = t.entry_set.all() #get all corresponding entries to that topic

for e in entries:
    print(e) #don't need to have a .text here because of the string line in the "models.py"
