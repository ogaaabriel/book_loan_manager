from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.UserPage.as_view(), name="userpage"),
    path(
        "entrar/",
        LoginView.as_view(
            redirect_authenticated_user=True,
            extra_context={"form_title": "Entre na sua conta", "btn_value": "Entrar"},
            template_name="form.html",
        ),
        name="login",
    ),
    path("sair/", LogoutView.as_view(), name="logout"),
    path("cadastrar_usuario/", views.Signup.as_view(), name="signup"),
]
