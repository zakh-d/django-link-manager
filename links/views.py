from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from links.forms import CollectionCreationForm
from links.models import Collection, Subscription


class LoginRedirect(LoginRequiredMixin):
    login_url = '/accounts/login'


class MyCollectionsView(LoginRedirect, generic.ListView):
    model = Collection
    context_object_name = "collection"
    template_name = 'collection/list.html'

    def get_queryset(self):
        return self.request.user.my_collections.all()


class MySubscriptionView(MyCollectionsView):

    def get_queryset(self):
        return list(map(lambda s: s.collection, self.request.user.my_subscriptions.all()))


class DetailCollectionView(LoginRedirect, generic.DetailView):
    model = Collection
    context_object_name = "collection"
    template_name = 'collection/detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['is_holder'] = self.object.holder == self.request.user
        try:
            Subscription.objects.get(collection=self.object, user=self.request.user)
            data['is_subscribed'] = True
        except Subscription.DoesNotExist:
            data['is_subscribed'] = False
        return data


class CreateCollectionView(LoginRedirect, generic.CreateView):
    model = Collection
    template_name = "collection/create.html"

    def get_form(self, **kwargs):
        return CollectionCreationForm(self.request.user, **kwargs)
