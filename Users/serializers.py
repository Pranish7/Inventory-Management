from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from Users.models import CustomUser 
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
# from django.contrib.auth.models import Group, Permission
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from Users.models import CustomUser as User
import re

class CustomUsersSerializer(ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields=('id','email','username', 'first_name', 'middle_name', 'last_name', 'contact_no', 'password','password2', 'gender','photo','is_active', 'is_staff')
        read_only = ('created_at', 'is_active', 'is_staff', 'auth_provider', 'username') 

    def validate(self, attrs):

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        if len(attrs['password']) < 6:
            raise ValidationError('Password must be at least 6 characters long')

        # if attrs['username'] != attrs['username'][:1].upper():
        #     raise serializers.ValidationError({"username": "Please put first letter"})

        if not re.findall('[A-Z]', attrs['username']):
            raise ValidationError("The username must contain at least 1 uppercase letter, A-Z.")

        if not re.findall('[a-z]', attrs['username']):
            raise ValidationError("The username must contain at least 1 lowercase letter, a-z.")

        if not re.findall('[0-9]', attrs['username']):
            raise ValidationError(("The username must contain at least 1 number, 0-9."))

        if ' ' in attrs['username']:
            raise ValidationError('username should not contain any space')
        return attrs


    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            middle_name=validated_data[ 'middle_name'],
            last_name=validated_data['last_name'],
            contact_no=validated_data['contact_no'],
            # group=validated_data['group'],
            gender=validated_data['gender'],
            is_staff=validated_data['is_staff'],
            photo=validated_data['photo'],
        )

        user.set_password(validated_data['password'])
        user.is_active = True
        user.save() 
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            if User.objects.filter(email=email).exists():
                user = authenticate(email=email, password=password)

                if user:
                    if user.is_active:
                        data["user"] = user
                    else:
                        msg = "Please verify your email"
                        raise serializers.ValidationError(msg)
                else:
                    raise APIException({'password': ['Incorrect Password']})
            else:
                raise APIException({'email': ['Email not registered']})
        else:
            msg = "Please provide email and password"
            raise serializers.ValidationError(msg)

        return data

# class ProfileSerializer(serializers.Serializer):
#     class Meta:
#         model = CustomUser
#         fields=('email','username', 'first_name', 'middle_name', 'last_name', 'contact_no', 'gender','photo')