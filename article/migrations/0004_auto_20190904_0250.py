# Generated by Django 2.2.1 on 2019-09-03 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190904_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='preview',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True, verbose_name='Önizleme(Anasayfada Gözükecek Kısım)'),
        ),
    ]
