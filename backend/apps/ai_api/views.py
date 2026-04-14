from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OutputSerializer, PreferencesSerializer
from .services import GemService
from .models import Output, Preferences

# Create your views here.

class OutputView(APIView):

    def get(self, request):
        output = Output.objects.all()
        serializer = OutputSerializer(output, many=True)
        return Response(serializer.data)

    def post(self, request):
        input = request.data.get("input")
        output = GemService.generate_text(input)
        serializer = OutputSerializer(data={"input": input,"output": output})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PreferencesView(APIView):

    def get(self, request):
        preference = Preferences.objects.all()
        serializer = PreferencesSerializer(preference, many=True)
        return Response(serializer.data)

    def post(self, request):
        city_state = request.data.get("city_state")
        type = request.data.get("type")
        recipe = GemService.generate_text(city_state, type)
        serializer = PreferencesSerializer(data={"city_state": city_state,"type": type, "recipe":recipe})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#     def post(self, request):
#         output = GemService.generate_text()
#         serializer = OutputSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(output, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   def get(self, request):
#         output = Output.objects.all()
#         serializer = OutputSerializer(output, many=True)
#         return Response(serializer.data)