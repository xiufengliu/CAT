# Generated by Django 2.2.12 on 2021-04-08 15:17

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey3rd', '0012_auto_20210408_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='s11_gender',
            field=otree.db.models.StringField(choices=[['female', 'Kvinde'], ['male', 'Mand']], max_length=10000, null=True),
        ),
    ]
