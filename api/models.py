
from django.db import models

class Note(models.Model):
    body= models.TextField(null=True, blank=True)
    updated= models.DateTimeField(auto_now=True)  # take a time stamp of when a note is updated
    creared= models.DateField(auto_now_add= True) # take a time stamp when the note is first created.

    def __str__(self):
        return self.body[0:50]


