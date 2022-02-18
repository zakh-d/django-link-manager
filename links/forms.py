from django import forms

from links.models import Collection


class CollectionCreationForm(forms.ModelForm):

    class Meta:
        model = Collection
        fields = ['name', 'is_public']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        name = self.cleaned_data['name']
        is_public = self.cleaned_data['is_public']
        new_collection = Collection(name=name, is_public=is_public, holder=self.user)
        new_collection.save()
        return new_collection
