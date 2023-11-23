

from rest_framework.serializers import ModelSerializer
from .models import UserAccount
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'first_name', 'email', 'last_name','password','is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        print("!!!!!!!!!!!!!!!!!!!")

        print(validated_data)

        print("!!!!!!!!!!!!!!!!!!!!!!")
        password = validated_data.pop('password', None)
        instance = self.Meta.model.objects.create(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        # Your custom update logic here
        print("--------update-----------")
        instance.id = validated_data.get('userId', instance.id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        # Update other fields as needed
        instance.save()
        return instance
class myTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(user.first_name,token)
        token['first_name'] = user.first_name
        token['email'] = user.email
        token['last_name'] = user.last_name
        if user.is_superuser:
            token['is_admin'] = user.is_superuser
        else:
            token['is_admin'] = False   

        return token