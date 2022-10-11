from rest_framework.serializers import ModelSerializer
from .models import Note

#Serialozer for Note Data class
class NoteSerializers(ModelSerializer):
    class Meta:
        model= Note
        fields= '__all__'