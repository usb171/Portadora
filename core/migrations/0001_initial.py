# Generated by Django 2.0.10 on 2019-01-28 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeSala', models.CharField(blank=True, max_length=120, null=True, verbose_name='Sala ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='Atualizado em')),
                ('userRx', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asdasd', to=settings.AUTH_USER_MODEL)),
                ('userTx', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
