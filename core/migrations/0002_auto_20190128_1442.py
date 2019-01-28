# Generated by Django 2.0.10 on 2019-01-28 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='userRx',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userRX', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sala',
            name='userTx',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userTX', to=settings.AUTH_USER_MODEL),
        ),
    ]
