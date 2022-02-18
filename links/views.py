from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from links.forms import CollectionCreationForm
from links.models import Collection, Subscription


class LoginRedirect(LoginRequiredMixin):
    login_url = '/accounts/login'


class MyCollectionsView(LoginRedirect, generic.ListView):
    model = Collection
    context_object_name = "collections"
    template_name = 'collection/list.html'

    def get_queryset(self):
        return self.request.user.my_collections.all()


class MySubscriptionView(MyCollectionsView):

    def get_queryset(self):
        return list(map(lambda s: s.collection, self.request.user.my_subscriptions.all()))


class DetailCollectionView(LoginRedirect, PermissionRequiredMixin, generic.DetailView):
    model = Collection
    context_object_name = "collection"
    template_name = 'collection/detail.html'

    def has_permission(self):
        collection = self.get_object()
        return collection.is_public or collection.holder == self.request.user

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
    form_class = CollectionCreationForm

    def get_form_kwargs(self):
        kwargs = super(CreateCollectionView, self).get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs


def create_delete_subscription(request):
    if request.method == "POST":
        collection = Collection.objects.get(id=request.POST['collection_id'])
        try:

            existing_subscription = Subscription.objects.get(collection=collection, user=request.user)
            existing_subscription.delete()

        except Subscription.DoesNotExist:

            new_subscription = Subscription(collection=collection, user=request.user)
            new_subscription.save()

        finally:
            return HttpResponseRedirect(reverse('subscriptions'))

    else:
        return HttpResponseNotAllowed('Method not allowed')
