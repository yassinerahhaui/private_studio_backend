# Generated by Django 4.2.2 on 2023-07-22 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_studio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupe',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Coupe',
        ),
    ]