# Generated by Django 2.1.3 on 2018-11-27 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20181126_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='autorisation',
            field=models.BooleanField(default=True, verbose_name='Autorisation des commentaires'),
        ),
        migrations.AlterField(
            model_name='marker',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
