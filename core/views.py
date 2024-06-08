from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.utils.translation import gettext_lazy as _
from core.forms import PlayerModelForm, GameModelForm
from core.models import PlayerModel, GameModel


class PlayerModelListView(ListView):
    template_name = "dashboard/players.html"
    queryset = PlayerModel.objects.order_by("-pk")


class PlayerModelDeleteView(DeleteView):
    template_name = "dashboard/players.html"
    queryset = PlayerModel.objects.order_by("-pk")

    def form_valid(self, form):
        form = super().form_valid(form)
        messages.success(self.request, _("The player has been deleted"))
        return form

    def get_success_url(self):
        return reverse("core:dash-player-list")


class PlayerModelCreateView(CreateView):
    template_name = "dashboard/form.html"
    queryset = PlayerModel.objects.order_by("-pk")
    form_class = PlayerModelForm

    def get_success_url(self):
        messages.success(self.request, _("The player has been created"))
        return reverse("core:dash-player-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = _("Create")
        context["model_name"] = _("Player")
        return context


class PlayerModelUpdateView(UpdateView):
    template_name = "dashboard/form.html"
    queryset = PlayerModel.objects.order_by("-pk")
    form_class = PlayerModelForm

    def get_success_url(self):
        messages.success(self.request, _("The player has been updated"))
        return reverse("core:dash-player-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = _("Update")
        context["model_name"] = _("Player")
        return context


class GameModelListView(ListView):
    template_name = "dashboard/games.html"
    queryset = GameModel.objects.order_by("-date_played")


class GameModelDeleteView(DeleteView):
    template_name = "dashboard/games.html"
    queryset = GameModel.objects.order_by("-date_played")

    def form_valid(self, form):
        form = super().form_valid(form)
        messages.success(self.request, _("The game has been deleted"))
        return form

    def get_success_url(self):
        return reverse("core:dash-game-list")


class GameModelCreateView(CreateView):
    template_name = "dashboard/form.html"
    queryset = GameModel.objects.order_by("-date_played")
    form_class = GameModelForm

    def get_success_url(self):
        messages.success(self.request, _("The game has been created"))
        return reverse("core:dash-game-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = _("Create")
        context["model_name"] = _("Game")
        return context


class GameModelUpdateView(UpdateView):
    template_name = "dashboard/form.html"
    queryset = GameModel.objects.order_by("-date_played")
    form_class = GameModelForm

    def get_success_url(self):
        messages.success(self.request, _("The game has been updated"))
        return reverse("core:dash-game-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = _("Update")
        context["model_name"] = _("Game")
        return context
