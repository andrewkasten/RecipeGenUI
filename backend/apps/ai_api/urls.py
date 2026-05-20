from django.urls import path
from .views import RecipeView

urlpatterns = [
    # path('gem', OutputView.as_view()),
    path('gem/recipe', RecipeView.as_view()),
    
]


