# Generated by Django 4.2.8 on 2023-12-26 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]