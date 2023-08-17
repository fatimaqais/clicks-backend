from django.urls import path
from events import views

urlpatterns = [
    path('events/', views.EventsList.as_view()),
    path('events/<int:pk>', views.EventsDetail.as_view()),
]
