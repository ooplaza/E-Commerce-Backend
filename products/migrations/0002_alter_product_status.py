# Generated by Django 4.2.4 on 2023-09-28 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], max_length=1),
        ),
    ]
