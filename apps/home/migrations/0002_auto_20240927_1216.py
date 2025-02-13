# Generated by Django 3.2.11 on 2024-09-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('tel', models.CharField(max_length=20)),
                ('sirket', models.CharField(max_length=500)),
                ('posta', models.CharField(max_length=10)),
                ('sehir', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=1005)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='StajUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=300)),
                ('password', models.CharField(max_length=20)),
                ('password_regen', models.CharField(blank=True, max_length=20)),
                ('create_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Register',
            },
        ),
        migrations.AlterModelTable(
            name='contact',
            table=None,
        ),
    ]
