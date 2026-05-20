from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OutputSerializer
from .services import GemRecipeService
from .models import Output



# Create your views here.

class OutputView(APIView):
    def get(self, request):
        output = Output.objects.all()
        serializer = OutputSerializer(Output, many=True)
        return Response(serializer.data)

def post(self, request):
        try:
            Output = GemRecipeService.generate_recipe()
        except Exception as e:
            print("GemRecipeService failed: %s", e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = OutputSerializer(data={"explained": Output})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Serializer errors: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

