from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Superhero
from .serializers import Superhero_serializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def superhero_list(request):
    if request.method == 'GET':
        superheros = Superhero.objects.all()
        serializer = Superhero_serializer(superheros, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Superhero_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
