from django.conf.urls import url
from token_based_app.views import LoginView,LogoutView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    url('api/vl/auth/login/', LoginView.as_view()),
    url('api/vl/auth/logout/', LogoutView.as_view()),

]    