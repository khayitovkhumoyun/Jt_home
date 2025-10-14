from django.urls import path


from .views import *

urlpatterns = [
    path("languages/", LanguageAPIView.as_view(), name="languages"),
    path("pageApi/<int:lan_pk>/", PageApi.as_view()),
    path("pages/", PageModelsAPIView.as_view(), name="pages"),
    path("contents/", ContentAPIView.as_view(), name="contents"),
    path("texts/", ContentTextAPIView.as_view(), name="texts"),
    path("files/", ContentFileAPIView.as_view(), name="files"),
    path("images/", ContentImageAPIView.as_view(), name="images"),
    path("videos/", ContentVideoAPIView.as_view(), name="videos"),
    path("languages/<int:pk>/", LanguageDetailAPIView.as_view(), name="language-detail"),

    # path("pages/", PageListCreateAPIView.as_view(), name="page-list"),
    path("pages/<int:pk>/", PageDetailAPIView.as_view(), name="page-detail"),

    # path("contents/", ContentListCreateAPIView.as_view(), name="content-list"),
    path("contents/<int:pk>/", ContentDetailAPIView.as_view(), name="content-detail"),

    # path("texts/", ContentTextListCreateAPIView.as_view(), name="text-list"),
    path("texts/<int:pk>/", ContentTextDetailAPIView.as_view(), name="text-detail"),
]
