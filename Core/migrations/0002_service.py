# Generated by Django 5.0.6 on 2024-07-08 05:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Status', models.IntegerField(default=1)),
                ('Title', models.CharField(max_length=50)),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Core.servicecategory')),
            ],
        ),
    ]