# Generated by Django 4.1.6 on 2023-02-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='created',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='todo',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]