# from click import style
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password









class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user



# class RegistartionsSerializer(serializers.ModelSerializer):
#     password2=serializers.charField(style={'input__type':'password'},write_only=True)
#     class Meta:
#         model = Account
#         fields = ['id', 'email', 'username','password','password2']

#         extra_kwargs={
#             'password':{'write_only':True}
#         }
#     def save(self):
#         account = Account(
#             email=self.validated_data['email'],
#             username= self.validated_data['username'],

#         )  

#         password=self.validate_data['password']
#         password2 =self.validate_data['password2']
#         if password != password2:
#             raise serializers.validationsErrorr({'password':'passwords must match'})
#         account.set_password(password)
#         account.save()    
#         return account
