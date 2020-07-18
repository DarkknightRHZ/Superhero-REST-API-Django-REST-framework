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

@csrf_exempt
def superhero_detail(request, id):
    try:
        superhero = Superhero.objects.get(hero_id=id)

    except Superhero.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Superhero_serializer(superhero)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Superhero_serializer(superhero, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        superhero.delete()
        return HttpResponse(status=204)

