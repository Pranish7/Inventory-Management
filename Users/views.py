import json
from django.core import serializers
from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import Group, Permission
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.tokens import default_token_generator
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from Users.models import CustomUser as User
from django.core.mail import send_mail, EmailMultiAlternatives, BadHeaderError
from django.contrib import messages
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .serializers import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import base64
from rest_framework.views import APIView
from django.utils.timezone import now
from django.contrib.auth import login, logout
# from rest_framework.filters import DjangoFilterBackend
from django.core.cache import cache
# import jwt
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import action
from django import template
# from django.utils.encoding import force_bytes, force_text

class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUsersSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         data = serializer.data
    #         for d in data:
    #             user = User.objects.get(email=d['email'])
    #             d['permissions'] = user.get_user_permissions()
    #         return self.get_paginated_response(data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     data = serializer.data
    #     for d in data:
    #         # user = User.objects.get(email=d['email'])
    #         user = User.objects.get(email=self.request.user)
    #         d['permissions'] = user.get_user_permissions()
    #     return Response(data)


    def get_queryset(self):
            # import pdb;pdb.set_trace()
            return self.queryset
            if self.request.user.is_superuser:
                return User.objects.all()
            else:
                return User.objects.filter(email = self.request.user)

        
    @action(methods=['get'], detail=False)
    def profile(self, request,*args, **kwargs):
        try:
            user = request.user
            serializer = CustomUsersSerializer(user)
            result = serializer.data
            result.pop('password')
            result['permission']=user.get_group_permissions()
            return Response(result, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'No detail found for the request user'})


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'message': 'Enter credentials to login'}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # now = datetime.datetime.now()
        # request.user.authenticate()
        # authenticate(username=user, password=pwd)
        # count = User.objects.get(email=user.email)
        # count.logcount += 1
        # count.save()
        # import pdb;pdb.set_trace()
        login(request, user)
        cache.set('user',user)
        token, created = Token.objects.get_or_create(user=user)
        # jwt_token=jwt.encode({"token":token.key},settings.SECRET_KEY, algorithm="HS512")
        response = Response({
            # "jwt":jwt_token,
            'token': token.key,
            'email': user.email,
            'first_name':user.first_name,
            'middle_name':user.middle_name,
            'last_name':user.last_name,
            'contact_no':user.contact_no,
            'gender':user.gender,
            # 'photo':user.photo,
            'is_active': user.is_active,
            'is_staff':user.is_staff,
            # 'is_verified': user.is_verified,

        }, status=status.HTTP_200_OK)
        response.set_cookie('auth_token', token, httponly=True, samesite='Lax')
        return response

class UserLogoutView(APIView):
    def post(self,request,format=None): 
        # count=User.objects.get(email=request.user.email)
        # count.logcount-=1cd
        # count.save()
        token=Token.objects.get(user=request.user)
        deletetoken(token)
        logout(request)
        return Response({'detail':f"Successfully logout"},status=204)