from rest_framework import serializers
from ..models import User
class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(label='Confirm Password')
    
    class Meta:
        model=User
        fields=('email','username','first_name','last_name','password','password2')
    

    def save(self, *args, **kwargs):
        if self.validated_data.get('password') != self.validated_data.get('password2'):
            raise serializers.ValidationError( {"password": "passwords do not match"} )

        user=User.objects.create_user(
        email=self.validated_data.get('email'),
        password=self.validated_data.get('password'),
        username=self.validated_data.get('password'))
        
        return user


