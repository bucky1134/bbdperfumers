# Generated by Django 2.1.7 on 2019-05-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attar',
            name='maxprice',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
