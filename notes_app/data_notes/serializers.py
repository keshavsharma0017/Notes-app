from .models import Notes_Attributes
from rest_framework.serializers import ModelSerializer

class NotesSerializer(ModelSerializer):
    class Meta:
        model = Notes_Attributes
        fields = '__all__'