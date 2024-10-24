from custom_auth.views import (
    create_user, login, logout, setup_password, request_password_reset, 
    reset_password, change_password
)
from ninja import Router

auth_router = Router()

@auth_router.post("/register/")
def register(request, payload):
    return create_user(request, payload)

@auth_router.post("/login/")
def login(request, payload):
    return login(request, payload)

@auth_router.post("/logout/")
def logout(request):
    return logout(request)

@auth_router.post("/password-reset-request/")
def request_password_reset(request, payload):
    return request_password_reset(request, payload)

@auth_router.post("/password-reset/{uidb64}/{token}/")
def reset_password(request, uidb64, token, payload):
    return reset_password(request, uidb64, token, payload)

@auth_router.post("/setup-password/{token}/")
def setup_password(request, token, payload):
    return setup_password(request, token, payload)

@auth_router.post("/change-password/")
def change_password(request, payload):
    return change_password(request, payload)