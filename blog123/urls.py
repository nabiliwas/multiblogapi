from django.urls import include, path
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

