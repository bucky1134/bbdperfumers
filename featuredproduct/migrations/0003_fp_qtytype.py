# Generated by Django 2.1.7 on 2019-05-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('featuredproduct', '0002_auto_20190502_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='fp',
            name='qtytype',
            field=models.TextField(blank=True),
        ),
    ]
