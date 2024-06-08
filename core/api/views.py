from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView

from core.models import PlayerModel, GameModel
from core.api.serializers import PlayerModelSerializer, GameModelSerializer
from core.api.filters import PlayerModelFilter, GameModelFilter


class CachedListCreateAPIView(ListCreateAPIView):
    """
    Base view with caching operations.
    """

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PlayerListCreateAPIView(CachedListCreateAPIView):
    """
    List and create PlayerModel instances with caching.
    """

    queryset = PlayerModel.objects.order_by("-pk")
    serializer_class = PlayerModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlayerModelFilter


class GameModelListCreateAPIView(CachedListCreateAPIView):
    """
    List and create GameModel instances with caching.
    """

    queryset = GameModel.objects.order_by("-date_played")
    serializer_class = GameModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GameModelFilter
