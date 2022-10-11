from django.contrib import admin

# To have the model inside the admin site, the model needs to be registered here.

from .models import Note

admin.site.register(Note)
