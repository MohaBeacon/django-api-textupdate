from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data
from .serializer import DataSerializer

# Create your views here.
@api_view(['GET','POST'])
def getData(request):
    if request.method == 'GET':
        app = Data.objects.last()
        serializer = DataSerializer(app)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
