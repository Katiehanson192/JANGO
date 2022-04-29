from django.urls import path


from . import views


app_name= 'MainApp'

urlpatterns = [
    path('', views.index, name='index'), #name = always same name as view
    path("topics", views.topics, name='topics'), #these are the pages for the website
    path('topics/<int:topic_id>/', views.topic, name='topic'), #ID = primary key
    path('new_topic/', views.new_topic, name='new_topic'),
]
