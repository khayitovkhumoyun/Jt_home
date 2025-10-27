from django.urls import path, include

from .views import *
from rest_framework.routers import DefaultRouter
from .views import (
    ContentViewSet, ContentTextViewSet, ContentFileViewSet,
    ContentImageViewSet, ContentVideoViewSet,
    NewsViewSet, NewsTextViewSet, NewsFileViewSet,
    NewsImageViewSet, NewsVideoViewSet, NewsTypeViewSet
)

router = DefaultRouter()
#
# # CONTENT
router.register(r'contents', ContentViewSet)
router.register(r'content-texts', ContentTextViewSet)
router.register(r'content-files', ContentFileViewSet)
router.register(r'content-images', ContentImageViewSet)
router.register(r'content-videos', ContentVideoViewSet)

# NEWS
router.register(r'news-types', NewsTypeViewSet)
router.register(r'news', NewsViewSet)
router.register(r'news-texts', NewsTextViewSet)
router.register(r'news-files', NewsFileViewSet)
router.register(r'news-images', NewsImageViewSet)
router.register(r'news-videos', NewsVideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("languages/", LanguageAPIView.as_view(), name="languages"),
    path("pageApi/<int:lan_pk>/", PageApi.as_view()),
    path("pages/", PageModelsAPIView.as_view(), name="pages"),
    path("contents/", ContentAPIView.as_view(), name="contents"),
    path("texts/", ContentTextAPIView.as_view(), name="texts"),

    path("languages/<int:pk>/", LanguageDetailAPIView.as_view(), name="language-detail"),

    # path("pages/", PageListCreateAPIView.as_view(), name="page-list"),
    path("pages/<int:pk>/", PageDetailAPIView.as_view(), name="page-detail"),

    # path("contents/", ContentListCreateAPIView.as_view(), name="content-list"),
    path("contents/<int:pk>/", ContentDetailAPIView.as_view(), name="content-detail"),

    # path("texts/", ContentTextListCreateAPIView.as_view(), name="text-list"),
    path("texts/<int:pk>/", ContentTextDetailAPIView.as_view(), name="text-detail"),
    path('news/type/<str:type_title>/', NewsByTypeAPIView.as_view(), name='news-by-type'),
    path('news/<str:title>/', NewsApiView.as_view(), name='news-title'),
    path('content/<str:title>/', ContentByTitleAPIView.as_view(), name='content-by-title'),
]
