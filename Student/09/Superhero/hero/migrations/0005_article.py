# Generated by Django 5.1.2 on 2024-12-07 00:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0004_superhero_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('publishdate', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='hero.creator')),
            ],
        ),
    ]
