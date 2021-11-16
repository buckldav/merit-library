from django.urls import path

from library.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)
from library.users.api.views import TestView

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("test/", TestView.as_view, name='test'),
]
