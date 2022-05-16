# Generated by Django 3.2.8 on 2022-03-25 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='group',
            name='description_html',
            field=models.TextField(blank=True, default='', editable=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
