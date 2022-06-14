# Generated by Django 4.0.4 on 2022-06-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='catalog/images/')),
                ('size', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
    ]