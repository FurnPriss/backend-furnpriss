# Generated by Django 3.2.13 on 2022-06-14 12:17

from django.db import migrations, models
import manager.generators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_usermodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.CharField(default=manager.generators.get_default_id, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
    ]