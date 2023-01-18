# Generated by Django 4.1.5 on 2023-01-18 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=250)),
                ('logo', models.ImageField(upload_to='')),
                ('new', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('position', models.CharField(max_length=250)),
                ('level', models.CharField(choices=[('Senior level', 'Senior level'), ('Mid level', 'Mid level'), ('Entry level', 'Entry level'), ('No experience required', 'No experience required')], max_length=250, verbose_name='Level')),
                ('contract', models.CharField(choices=[('Full-time', 'Full-time'), ('Contract', 'Contract'), ('Part-time', 'Part-time'), ('Temporary', 'Temporary')], max_length=20, verbose_name='Contract')),
                ('location', models.CharField(max_length=250)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.language')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.role')),
                ('tools', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tool')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
