# Generated by Django 5.0.6 on 2024-06-02 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
