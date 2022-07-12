from django.urls import path,include
from .views import ConsumerView
urlpatterns = [
    path('consumer/',ConsumerView.as_view())
]