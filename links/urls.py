from django.urls import path

from links.views import DetailCollectionView, MySubscriptionView, CreateCollectionView

urlpatterns = [
    path('<uuid:pk>/', DetailCollectionView.as_view(), name="collection_detail"),
    path('subscriptions/', MySubscriptionView.as_view(), name="subscriptions"),
    path('create/', CreateCollectionView.as_view(), name="create_collection")
]