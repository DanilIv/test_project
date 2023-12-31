# Generated by Django 3.2.20 on 2023-09-04 12:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('check_execute', models.BooleanField(default=False)),
            ],
        ),
    ]
