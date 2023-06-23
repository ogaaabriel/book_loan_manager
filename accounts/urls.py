from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "accounts"

urlpatterns = [
    path(
        "entrar/",
        LoginView.as_view(
            redirect_authenticated_user=True,
            template_name="accounts/login.html",
        ),
        name="login",
    ),
    path("sair/", LogoutView.as_view(), name="logout"),
    path("cadastrar_usuario/", views.Signup.as_view(), name="signup"),
    path("usuarios/", views.ListUsersView.as_view(), name="users"),
]
