# Generated by Django 4.2.1 on 2023-05-23 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0011_alter_permission_permission_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_to_course',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_to_jop',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_to_role',
        ),
        migrations.AlterField(
            model_name='role',
            name='role_to_user',
            field=models.ManyToManyField(through='users.UserRoles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userroles',
            name='user_rel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]