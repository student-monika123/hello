# Generated by Django 5.0.2 on 2024-03-12 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('emmail', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
