from django.urls import path
from likeposts import views

urlpatterns = [
    path('likes/', views.LikePostList.as_view()),
    path('likes/<int:pk>', views.LikePostDetail.as_view())
]
