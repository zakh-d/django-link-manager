# Generated by Django 4.0.2 on 2022-02-04 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('is_public', models.BooleanField(default=False)),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_collections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.collection')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='links.collection')),
            ],
        ),
    ]
