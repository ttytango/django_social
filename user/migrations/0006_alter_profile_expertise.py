# Generated by Django 3.2.9 on 2021-12-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20211202_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expertise',
            field=models.ManyToManyField(related_name='users', to='user.Expertise'),
        ),
    ]