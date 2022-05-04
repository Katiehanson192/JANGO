from django.urls import path


from . import views


app_name= 'MainApp'

urlpatterns = [
    path('', views.index, name='index'), #name = always same name as view
    path("topics/", views.topics, name='topics'), #these are the pages for the website
    path('topics/<int:topic_id>/', views.topic, name='topic'), #ID = primary key
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), #creating a new entry, needs to be under a topic to link the entry to
    path('edit_entry/<int:entry_id>/',views.edit_entry, name='edit_entry')
]
