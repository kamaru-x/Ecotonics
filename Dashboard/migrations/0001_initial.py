# Generated by Django 5.0.6 on 2024-06-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Status', models.CharField(default='PENDING', max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('Place', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=20)),
                ('Mail', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]