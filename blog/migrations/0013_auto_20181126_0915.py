# Generated by Django 2.1.3 on 2018-11-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_fileitem_file_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=4)),
                ('longitude', models.CharField(max_length=4)),
                ('adresse', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='adress',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]