# Generated by Django 2.2.1 on 2019-09-03 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='preview',
            field=models.CharField(default=' ', max_length=100, verbose_name='Önizleme'),
        ),
    ]