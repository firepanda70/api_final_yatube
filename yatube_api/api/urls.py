from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'follow', FollowViewSet, basename='follow')
router_v1.register(r'posts', PostViewSet, basename='post')
router_v1.register(r'groups', GroupViewSet, basename='group')
router_v1.register(r'posts\/(?P<post_id>\d+)\/comments',
                   CommentViewSet, basename='comment')
urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('', include('djoser.urls.jwt')),
]
