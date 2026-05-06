import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RecipeSerializer
from .services import GemRecipeService
from .models import Recipe

logger = logging.getLogger(__name__)


class RecipeView(APIView):

    def get(self, request):
        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(recipe, many=True)
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
        serializer = RecipeSerializer(data={"state": state, "type": type, "recipe": recipe})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Serializer errors: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



