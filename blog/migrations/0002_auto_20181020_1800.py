# Generated by Django 2.1.2 on 2018-10-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content', 
            field=models.TextField(max_length=150),

        ),
    ]
