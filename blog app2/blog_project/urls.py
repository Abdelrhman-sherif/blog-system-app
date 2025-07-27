from django.contrib import admin
from django.urls import path, include
from blog import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/posts/<int:post_id>/comments/', views.CommentListCreateAPIView.as_view(), name='comment-list-create'),
]
