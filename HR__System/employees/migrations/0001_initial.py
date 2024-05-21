# Generated by Django 5.0.6 on 2024-05-20 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('group', models.CharField(choices=[('HR', 'HR'), ('Normal', 'Normal Employee')], max_length=20)),
            ],
        ),
    ]
