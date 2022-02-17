from django.contrib import admin

from links.models import Link, Collection, Subscription


class LinksInlines(admin.TabularInline):
    model = Link


class CollectionAdmin(admin.ModelAdmin):
    inlines = [
        LinksInlines,
    ]


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Subscription)
