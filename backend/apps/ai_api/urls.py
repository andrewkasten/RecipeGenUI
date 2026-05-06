from django.urls import path
from .views import OutputView, PreferencesView, WeatherNoteView

urlpatterns = [
    # path('gem', OutputView.as_view()),
    path('gem/recipe', PreferencesView.as_view()),
    
]


