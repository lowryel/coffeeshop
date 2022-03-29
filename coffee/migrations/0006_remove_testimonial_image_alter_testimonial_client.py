# Generated by Django 4.0.2 on 2022-03-18 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffee', '0005_orderbooking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='image',
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
