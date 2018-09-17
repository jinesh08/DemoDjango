import json, random
from rest_framework import status, mixins
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import viewsets

from demo_apis.models import *

class LoginRegisterViewSet(viewsets.ViewSet):

  @list_route(methods=['post'])
  def register(self, request):
    """
    ---
    parameters:
            - name: username
              description: Username to login
              required: false
              type: string
              paramType: form
            - name: password
              description: password of user
              required: false
              type: string
              paramType: form
    """
    response = {}

    # Check if username and password exist
    if not "username" in request.data:
    	response["result"] = 0
    	response["message"] = "Please enter a valid username"
    	return Response(response, status=status.HTTP_200_OK)

    if not "password" in request.data:
    	response["result"] = 0
    	response["message"] = "Please enter password"
    	return Response(response, status=status.HTTP_200_OK)

    credentials = Credentials()
    
    credentials.username = request.data['username']
    credentials.password = request.data['password']

    credentials.save()

    response["result"] = 1
    response["message"] = "User successfully created"
    
    return Response(response, status=status.HTTP_200_OK)


  @list_route(methods=['post'])
  def login(self, request):
    """
    ---
    parameters:
            - name: username
              description: Username to login
              required: false
              type: string
              paramType: form
            - name: password
              description: password of user
              required: false
              type: string
              paramType: form
    """
    response = {}

    # Check if username and password exist
    if not "username" in request.data:
    	response["result"] = 0
    	response["message"] = "Please enter a valid username"
    	return Response(response, status=status.HTTP_200_OK)

    if not "password" in request.data:
    	response["result"] = 0
    	response["message"] = "Please enter password"
    	return Response(response, status=status.HTTP_200_OK)

    if Credentials.objects.filter(username = request.data['username'], password = request.data['password']).exists():

    	response["result"] = 1
    	response["message"] = "successfully logged in"

    else:

    	response["result"] = 0
    	response["message"] = "Invalid credentials"
    
    return Response(response, status=status.HTTP_200_OK)

  @list_route(methods=['post'])
  def create_user(self, request):
    """
    ---
    parameters:
            - name: name
              description: name of user
              required: false
              type: string
              paramType: form
            - name: mobile
              description: mobile of user
              required: false
              type: string
              paramType: form
            - name: email
              description: email of user
              required: false
              type: string
              paramType: form
            - name: photo
              description: photo of user
              required: false
              type: file
              paramType: form  
    """
    response = {}

    # Check if username and password exist
    if not "name" in request.data:
      response["result"] = 0
      response["message"] = "Please enter a valid name"
      return Response(response, status=status.HTTP_200_OK)

    if not "mobile" in request.data:
      response["result"] = 0
      response["message"] = "Please enter mobile"
      return Response(response, status=status.HTTP_200_OK)

    if not User.objects.filter(name = request.data["name"], mobile = request.data["mobile"]).exists():
      user = User()

      user.name = request.data["name"]
      user.mobile = request.data["mobile"]
      if "email" in request.data:
        user.email = request.data["email"]

      if "photo" in request.FILES:
        user.user_photo = request.FILES["photo"]

      user.save()

      response["result"] = 1
      response["message"] = "User successfully created"

    else:

      response["result"] = 0
      response["message"] = "User already exists"
    
    return Response(response, status=status.HTTP_200_OK)