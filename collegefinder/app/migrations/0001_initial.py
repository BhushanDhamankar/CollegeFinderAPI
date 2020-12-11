# Generated by Django 3.0.5 on 2020-12-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='model_feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('checkbox', models.BooleanField()),
                ('feed', models.TextField(max_length=500)),
            ],
        ),
    ]