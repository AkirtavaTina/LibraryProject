# Generated by Django 5.1.3 on 2024-11-20 16:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='birth date'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default='', max_length=150, verbose_name='full name'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='personal_number',
            field=models.CharField(default='', max_length=20, unique=True, verbose_name='personal number'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff status'),
        ),
    ]
