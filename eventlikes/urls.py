from django.urls import path
from eventlikes import views

urlpatterns = [
    path('eventlikes/', views.LikeEventList.as_view()),
    path('eventlikes/<int:pk>', views.LikeEventDetail.as_view())
]
