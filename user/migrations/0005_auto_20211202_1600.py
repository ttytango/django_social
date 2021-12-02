# Generated by Django 3.2.9 on 2021-12-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_profile_expertise'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'technologies'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='expertise',
        ),
        migrations.AddField(
            model_name='profile',
            name='expertise',
            field=models.ManyToManyField(related_name='skills', to='user.Expertise'),
        ),
    ]