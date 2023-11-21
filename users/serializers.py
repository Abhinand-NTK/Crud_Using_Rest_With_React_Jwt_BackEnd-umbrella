# from django.contrib.auth.password_validation import validate_password 
# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from django.core import exceptions
# User = get_user_model()
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name','last_name','email','password')

#     def validate(self, data):
#         user = User(**data)
#         password = data.get ('password')
#         try:
#             validate_password(password,user)
#         except exceptions.ValidationError as e:

#             serializer_errors = serializers.as_serializer_error(e)
#             raise exceptions.ValidationError({'password':serializer_errors['non_field_errors']})
        
#         return data


#     def create(self, validated_data):
#         user=User.objects.create_user(
#             first_name =  validated_data['first_name'],
#             last_name =  validated_data['last_name'],   
#             email =  validated_data['email'],
#             password =  validated_data['password'],
#             )
#         return user 
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name','last_name','email','is_superuser')

# # class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
# #     @classmethod  
# #     def get_token(cls, user):
# #         token = super().get_token(user)

# #         # Add custom claims to the token payload
# #         token['is_superuser'] = user.is_superuser
# #         # Add more custom claims if needed

# #         return token

from rest_framework.serializers import ModelSerializer
from .models import UserAccount
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'first_name', 'email', 'last_name','password']
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