# Generated by Django 4.0.4 on 2022-05-05 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0003_remove_tutor_thumbnail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'categories'},
        ),
    ]