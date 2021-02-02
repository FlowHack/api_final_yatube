from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from api.settings import MainViewSetListCreate

from api.models import Comment, Post, Follow, Group
from api.serializers import CommentSerializer, PostSerializer, FollowSerializer, GroupSerializer
from api.permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments


class FollowViewSet(MainViewSetListCreate):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username',)

    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)


class GroupViewSet(MainViewSetListCreate):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
