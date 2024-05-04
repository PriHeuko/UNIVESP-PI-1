# Generated by Django 5.0.4 on 2024-05-02 23:56

import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='produtos', variations={'thumb': (124, 124)}, verbose_name='Imagem'),
        ),
    ]
