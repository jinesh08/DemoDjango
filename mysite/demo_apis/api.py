import json, random
from rest_framework import status, mixins
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import viewsets

from demo_apis.subapis.auth import *