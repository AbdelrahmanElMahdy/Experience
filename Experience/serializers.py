from rest_framework import serializers 
from .models import Experience,Rate

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

class UpdateRateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Rate
        fields=("message","rate","rate_category")

    def save(self,instance):
        instance.message=self.validated_data["message"],
        instance.rate=self.validated_data["rate"],
        instance.rate_category=self.validated_data["rate_category"]
        instance.save()
        return instance


class ExpRateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Rate
        fields="__all__"
    


class CreateRateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Rate
        fields=("message","rate","rate_category")
    
    def save(self,author,exPk):
        Rate.objects.create(
            author=author,
            experience=Experience.objects.get(id=exPk),
            message=self.validated_data["message"],
            rate=self.validated_data["rate"],
            rate_category=self.validated_data["rate_category"]
        )