# Generated by Django 4.2.1 on 2023-05-23 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0005_remove_course_user_re_course_user_to_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='user_to_course',
            field=models.ManyToManyField(through='courses.CourseRegister', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='courseregister',
            name='user_rel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
