# Generated by Django 2.2.12 on 2021-04-02 19:43

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey2nd', '0010_auto_20210402_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email_addr',
            field=otree.db.models.StringField(blank=True, default='', max_length=10000, null=True, verbose_name=''),
        ),
    ]
