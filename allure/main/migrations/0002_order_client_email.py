# Generated by Django 3.0.11 on 2021-01-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта клиента'),
        ),
    ]