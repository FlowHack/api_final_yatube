from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

api_routers_v1 = DefaultRouter()
api_routers_v1.register('posts', PostViewSet, basename='posts')
api_routers_v1.register('group', GroupViewSet, basename='groups')
api_routers_v1.register('follow', FollowViewSet, basename='follow')
api_routers_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/', include(api_routers_v1.urls))
]

