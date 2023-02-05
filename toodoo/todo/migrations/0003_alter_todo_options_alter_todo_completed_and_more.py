# Generated by Django 4.1.6 on 2023-02-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_created_todo_created_date_todo_completed_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Задача выполнена'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Задача завершена'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Задача создана'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание задачи'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Задача'),
        ),
    ]
