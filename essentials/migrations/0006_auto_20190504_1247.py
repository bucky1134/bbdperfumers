# Generated by Django 2.1.7 on 2019-05-04 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essentials', '0005_essential_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='essential',
            old_name='variation',
            new_name='variation1',
        ),
        migrations.AddField(
            model_name='essential',
            name='variation2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='essential',
            name='variation3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='essential',
            name='variation4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='essential',
            name='variation5',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='essential',
            name='variation6',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='essential',
            name='variation7',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='essential',
            name='variation8',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='essential',
            name='variation9',
            field=models.TextField(blank=True),
        ),
    ]
