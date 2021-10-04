from django.shortcuts import render
from core.models import Contato
from core.serializers import ContatoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return render(request, 'index.html')


def getView(request):
    return render(request, 'get.html', )

def postView(request):
    return render(request, 'post.html')

def putView(request):
    return render(request, 'put.html')

def deleteView(request):
    return render(request, 'delete.html')




@api_view(['POST'])
def LibPost(request):
    serializer = LibSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def LibPut(request, pk):
    lib = Lib.objects.get(id=pk)
    serializer = LibSerializer(lib, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def LibDelete(request, pk):
    lib = Lib.objects.get(id=pk)
    lib.delete()
    return Response('Apagado')
