# Generated by Django 4.2.4 on 2023-08-17 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DNC', '0006_alter_samples_assosiation_alter_samples_cert_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samples',
            name='assosiation',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='cert',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='classification',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='contnum',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='cooperative',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='country',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='cropyear',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='customer',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='density',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='drymill',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='estgreenweight',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='exparrival',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='exporter',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='expprice',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='exptotalprice',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='expweight',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='expweightunit',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='farm',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='generalcomments',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='grade',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='iconum',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='id',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='samples',
            name='importer',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='location',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='moisture',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='samples',
            name='notes',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='othertrac',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='physicaldefects',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='proccessing',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='project',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='rating',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='refid',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='salenum',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='sampleweight',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='sampleweightunit',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='screensize',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='sensorial',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='sensorialdescriptors',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='stype',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='tracknum',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='varieties',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='wa',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='samples',
            name='wetmill',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
