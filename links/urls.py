from django.urls import path

from links.views import DetailCollectionView, MySubscriptionView, CreateCollectionView, create_delete_subscription

urlpatterns = [
    path('<uuid:pk>/', DetailCollectionView.as_view(), name="collection_detail"),
    path('subscriptions/', MySubscriptionView.as_view(), name="subscriptions"),
    path('subscriptions/cd', create_delete_subscription, name="subscriptions_cd"),  # Create Delete subscription
    path('create/', CreateCollectionView.as_view(), name="create_collection")
]