# Generated by Django 4.2.4 on 2023-08-17 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DNC', '0004_alter_samples_regdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samples',
            name='cid',
        ),
        migrations.AlterField(
            model_name='samples',
            name='id',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]
