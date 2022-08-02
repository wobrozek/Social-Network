
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API Routes
    path("posts",views.createPost, name="createPost"),
    path("posts/<int:post_id>",views.changePosts, name="changePosts"),
    path("posts/<str:type>",views.showPosts, name="showPosts"),

    path("post/<int:post_id>/comments",views.createComment, name="createComment"),
    path("comment/<int:post_id>/<int:comment_id>",views.changeComment, name="changeComment"),
    path("posts/<str:type>",views.showComment, name="showComment")
]
