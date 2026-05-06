import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OutputSerializer, PreferencesSerializer, WeatherNoteSerializer
from .services import GemService, GemRecipeService
from .models import Output, Preferences, WeatherNote

logger = logging.getLogger(__name__)

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
        state = request.data.get("state")
        type = request.data.get("type")
        if not state or not type:
            return Response({"error": "state and type are required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            recipe = GemRecipeService.generate_recipe(state, type)
        except Exception as e:
            logger.exception("GemRecipeService failed: %s", e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = PreferencesSerializer(data={"state": state, "type": type, "recipe": recipe})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Serializer errors: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



