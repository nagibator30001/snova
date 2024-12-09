from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.text.views import NewsListAPIView

router = DefaultRouter()
urlpatterns = [
    path("news_list", NewsListAPIView.as_view(), name='list_api')
]

urlpatterns += router.urls
