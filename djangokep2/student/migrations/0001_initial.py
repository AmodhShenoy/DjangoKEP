# Generated by Django 3.0.7 on 2020-11-06 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
