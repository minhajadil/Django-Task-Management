# Generated by Django 5.0 on 2024-01-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_taskcategory_task'),
        ('task', '0002_rename_is_completed_taskmodel_is_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='category',
            field=models.ManyToManyField(to='category.taskcategory'),
        ),
    ]
