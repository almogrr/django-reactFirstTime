from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView





def index(req):
    return JsonResponse('hello', safe=False)




class reactview (APIView):
    def get(self,req): #read
        output = [{ "desc": output.desc,
                    "price": output.price}
                for output in React.objects.all()]
        return Response(output)
    
    def post(self,req):
        serializer = ReactSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)