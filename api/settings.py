from rest_framework import viewsets, mixins


class MainViewSetListCreate(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    pass
