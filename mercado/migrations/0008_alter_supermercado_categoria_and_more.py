# Generated by Django 5.0.3 on 2024-03-14 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0007_alter_supermercado_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supermercado',
            name='categoria',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='supermercado',
            name='preço',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='supermercado',
            name='produto',
            field=models.CharField(default='none', max_length=50),
        ),
    ]
