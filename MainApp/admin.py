from django.contrib import admin

# Register your models here.
from .models import Topic #. in front of model = in same directory as currently using
from .models import Entry

admin.site.register(Topic)
admin.site.register(Entry)
pip