from django.urls import path
from eventreview import views

urlpatterns = [
    path('eventreviews/', views.ReviewList.as_view()),
    path('eventreviews/<int:pk>/', views.ReviewDetail.as_view())
]
