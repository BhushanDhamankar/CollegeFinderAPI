# Generated by Django 3.0.5 on 2020-12-10 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201208_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapping',
            name='branch_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Branch'),
        ),
        migrations.AlterField(
            model_name='mapping',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
        ),
        migrations.AlterField(
            model_name='mapping',
            name='college_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.College'),
        ),
    ]
