from tabnanny import verbose
from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:  #returns back result that you want returned
        return self.text #this gives the name of the topic
  
class Entry(models.Model): #associate Entry w/ many models??  #one topic can have multiple entries (1 to many relationship)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}" #returns first 50 characters of the entry in the text field
                            #whenever you call this method, everything it returns will be a string