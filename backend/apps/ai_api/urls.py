from django.urls import path, include
from .views import OutputView, PreferencesView

urlpatterns = [
    path('gem', OutputView.as_view()),
    path('gem', OutputView.as_view()),
]


