# Generated by Django 3.0.5 on 2020-12-11 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201211_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapping',
            name='collegeid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.College'),
        ),
    ]