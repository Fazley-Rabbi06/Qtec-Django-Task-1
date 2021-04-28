# Generated by Django 3.2 on 2021-04-27 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=264)),
                ('is_merchant', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, help_text='Determines Whether They Can Log in this Site or not', verbose_name='staff_status')),
                ('is_active', models.BooleanField(default=True, help_text='Determines Whether their Account Status is Active or not', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'User',
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=264)),
                ('address_1', models.TextField(blank=True, max_length=264)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('invoice_id', models.CharField(max_length=10, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='merchant', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Merchant',
                'db_table': 'Merchant',
            },
        ),
    ]
