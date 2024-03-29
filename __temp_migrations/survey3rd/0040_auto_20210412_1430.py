# Generated by Django 2.2.12 on 2021-04-12 12:30

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey3rd', '0039_auto_20210412_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='s110_desc_climate_event',
            field=otree.db.models.StringField(blank=True, default='', max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s111_likelihood_climent_event',
            field=otree.db.models.StringField(choices=[['highly unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly likely', 'højst sandsynligt']], max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s112_degree_or_disagree',
            field=otree.db.models.StringField(choices=[['strongly agree', 'meget enig'], ['agree', 'enig'], ['neutral', 'hverken enig eller uenig'], ['disagree', 'uenig'], ['strongly disagree', 'meget uenig']], max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s11_gender',
            field=otree.db.models.StringField(choices=[('female', 'Kvinde'), ('male', 'Mand')], max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s12_age',
            field=otree.db.models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s13_live_status',
            field=otree.db.models.StringField(choices=[('alone', 'Jeg bor alene'), ('with_partner', 'Je bor med min partner'), ('with_partner_and_children', 'Jeg bor med min partner og børn'), ('with_children', 'Jeg bor med mine børn')], max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s14_monthly_income',
            field=otree.db.models.StringField(choices=[['above 40k', '40.000DKK eller over'], ['between', 'Mellem 25.000DKK and 40.000DKK'], ['less 25k', '25.000DKK eller under']], max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s15_municipality',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s16_property_ownership',
            field=otree.db.models.StringField(choices=[['own', 'Ejerbolig'], ['rent', 'Leje'], ['others', 'Andet']], max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s17_is_flood_risk_zone',
            field=otree.db.models.StringField(choices=[['no', 'Nej. Ingen risiko'], ['medium', 'Ja. Mellem risiko'], ['high', 'Ja. Høj risiko']], max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s18_house_type',
            field=otree.db.models.StringField(choices=[['duplex', 'Etagebolig'], ['detached house', 'Parcelhus'], ['terraced house', 'Rækkehus'], ['others', 'Andet']], max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s19_is_exposed_climate_event',
            field=otree.db.models.StringField(choices=[['yes', 'Ja'], ['no', 'Nej']], max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s210_gettouchstranger',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s211_worry',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s212_wondering',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s213_goodimg',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s214_precise',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s215_agreeothers',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s216_talkothers',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s217_overcome',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s218_famous',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s219_lovepeople',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s21_lookpainting',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s220_dothings',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s221_staycalm',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s222_wellmanner',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s223_tear',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s224_soap',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s22_thingsinplace',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s23_remainunkind',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s24_nobodylikeme',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s25_afraidfeelingpain',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s26_hardtolie',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s27_sciboring',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s28_postponetask',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='s29_criticism',
            field=otree.db.models.IntegerField(choices=[(1, 'Meget enig'), (2, 'Enig'), (3, 'Hverken enig eller uenig'), (4, 'Uenig'), (5, 'Meget uenig')], null=True),
        ),
    ]
