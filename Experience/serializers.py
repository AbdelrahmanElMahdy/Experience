from rest_framework import serializers 
from .models import Experience

class CreatExpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Experience
        fields=("foundation","story")
    
    def save(self,author):
        Experience.objects.create(
            author=author,
            story=self.validated_data["story"],
            foundation=self.validated_data["foundation"]
        )

   
    

class ListExpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Experience
        fields="__all__"

class UpdateExpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Experience
        fields=("foundation","story")

    def save(self,instance):
        instance.story=self.validated_data['story']
        instance.foundation=self.validated_data['foundation']
        instance.save()
        return instance
    

