# Generated by Django 4.2 on 2023-04-11 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_student_qualification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='qualification',
        ),
    ]