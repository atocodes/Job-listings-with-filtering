# Generated by Django 4.1.5 on 2023-01-18 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_listing_contract_remove_listing_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='posted_at',
            field=models.DateTimeField(),
        ),
    ]