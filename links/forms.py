from django import forms

from links.models import Collection


class CollectionCreationForm(forms.ModelForm):

    class Meta:
        model = Collection
        fields = ['name']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)

    def save(self, commit=True):
        name = self.cleaned_data['name']
        new_collection = Collection(name=name, holder=self.user)
        new_collection.save()
        return new_collection
