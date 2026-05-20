from django.urls import path
from .views import OutputView

urlpatterns = [
    path('gem/design', OutputView.as_view()),
]


