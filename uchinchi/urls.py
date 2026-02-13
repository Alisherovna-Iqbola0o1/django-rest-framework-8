from django.urls import path
from .views import Salom1ListCreateAPIView, Salom2ListCreateAPIView, Salom3ListCreateAPIView, Salom4ListCreateAPIView, Salom5ListCreateAPIView

urlpatterns = [
    path("salom1/", Salom1ListCreateAPIView.as_view()),
    path("salom1/<int:pk>/", Salom1ListCreateAPIView.as_view()),

    path("salom2/", Salom2ListCreateAPIView.as_view()),
    path("salom2/<int:pk>/", Salom3ListCreateAPIView.as_view()),

    path("salom3/", Salom3ListCreateAPIView.as_view()),
    path("salom3/<int:pk>/", Salom3ListCreateAPIView.as_view()),

    path("salom4/", Salom4ListCreateAPIView.as_view()),
    path("salom4/", Salom4ListCreateAPIView.as_view()),

    path("salom5/", Salom5ListCreateAPIView.as_view()),
    path("salom5/<int:pk>/", Salom5ListCreateAPIView.as_view())
]