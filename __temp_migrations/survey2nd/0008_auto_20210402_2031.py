# Generated by Django 2.2.12 on 2021-04-02 18:31

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey2nd', '0007_auto_20210316_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='s19_is_exposed_climate_event',
            field=otree.db.models.StringField(choices=[['yes', 'Ja'], ['no', 'Nej']], max_length=10000, null=True, verbose_name='Har du, et familiemedlem eller ven været udsat for klimarelateret begivenheder (f.eks. oversvømmelse)?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s21_prefered_option',
            field=otree.db.models.StringField(choices=[['flatorcrown', 'Slå plat eller krone og vind 10.000 DKK med 50 procents sandsynlighed og 50 procents sandsynlighed for ingenting '], ['win5kddk', 'Vind 5.000 DKK med sikkerhed'], ['nomatter', 'Ligegyldigt, jeg synes begge muligheder er lige gode']], max_length=10000, null=True, verbose_name='Hvilken mulighed ville du foretrække?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s22_program_ab',
            field=otree.db.models.StringField(choices=[['progA', 'Scenarie A: 200 mennesker bliver reddet med sikkerhed'], ['progB', 'Scenarie B: Der er en tredjedel sandsynlighed for, at 600 mennesker bliver reddet, og to tredjedels sandsynlighed for, at ingen mennesker bliver reddet']], max_length=10000, null=True, verbose_name='Hvilke af de to scenarier vil du foretrække? '),
        ),
        migrations.AlterField(
            model_name='player',
            name='s23_program_cd',
            field=otree.db.models.StringField(choices=[['progC', 'Scenarie C: 400 mennesker vil omkomme'], ['progD', 'Scenarie D: Der er en tredjedel sandsynlighed for, at ingen mennesker vil omkomme og to tredjedele sandsynlighed for, at  600 mennesker vil omkomme']], max_length=10000, null=True, verbose_name='Hvilke af de to scenarier vil du foretrække? '),
        ),
        migrations.AlterField(
            model_name='player',
            name='s31_findsolution',
            field=otree.db.models.StringField(choices=[['strongly_agree', 'meget enig'], ['agree', 'enig'], ['n_agree_disagree', 'hverken enig eller uenig'], ['disagree', 'uenig'], ['strongdisagree', 'meget uenig']], max_length=10000, null=True, verbose_name='Jeg er i stand til at finde løsninger på problemstillinger, som opstår i min hverdag.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s32_findvalue',
            field=otree.db.models.StringField(choices=[['strongly_agree', 'meget enig'], ['agree', 'enig'], ['n_agree_disagree', 'hverken enig eller uenig'], ['disagree', 'uenig'], ['strongdisagree', 'meget uenig']], max_length=10000, null=True, verbose_name='Jeg er i stand til at finde værdi i selve håndtering af de problemstillinger, som jeg står over for i min hverdag.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s33_understand_issue',
            field=otree.db.models.StringField(choices=[['strongly_agree', 'meget enig'], ['agree', 'enig'], ['n_agree_disagree', 'hverken enig eller uenig'], ['disagree', 'uenig'], ['strongdisagree', 'meget uenig']], max_length=10000, null=True, verbose_name='Jeg er i stand til at forstå og forudsige de problemstillinger, som opstår i min hverdag.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s41_adversity',
            field=otree.db.models.StringField(choices=[['strongly_agree', 'meget enig'], ['agree', 'enig'], ['n_agree_disagree', 'hverken enig eller uenig'], ['disagree', 'uenig'], ['strongdisagree', 'meget uenig']], max_length=10000, null=True, verbose_name='De vil overkomme de udfordringer, som følger af oversvømmelsen.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s42_staycalm',
            field=otree.db.models.StringField(choices=[['strongly_agree', 'meget enig'], ['agree', 'enig'], ['n_agree_disagree', 'hverken enig eller uenig'], ['disagree', 'uenig'], ['strongdisagree', 'meget uenig']], max_length=10000, null=True, verbose_name='De vil bevare roen, imens de vil tage stilling til hvad de skal gøre.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s43_meaning_exp',
            field=otree.db.models.StringField(choices=[['strongly_agree', 'meget enig'], ['agree', 'enig'], ['n_agree_disagree', 'hverken enig eller uenig'], ['disagree', 'uenig'], ['strongdisagree', 'meget uenig']], max_length=10000, null=True, verbose_name='De vil finde mening i oplevelsen.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s510_takecredit',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… tage æren for en anden persons arbejde?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s511_rundownski',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… køre ned ad en skiløjpe, der er vanskeligere end dine evner rækker til?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s512_invest5perincome',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… investere 5% af din årsindtægt i en stærkt spekulativ aktie?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s513_whitewaterrafting',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… tage på white water rafting om foråret når strømmen er stærkest?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s514_wageonmatch',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… satse en dagløn på en sportskamp (f.eks. fodbold, boksning eller håndbold)?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s515_unsupportedsex',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… dyrke ubeskyttet sex?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s516_revealsecret',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… røbe en vens hemmelighed til en anden person?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s517_drivecarnobelt',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… køre i bil uden sele?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s518_investstartup',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… investere 10% af din årsindtægt i en nystartet virksomhed?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s519_learnparachute',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… lære at springe i faldskærm?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s51_diff_taste',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… indrømme, at du har en anderledes smag end dine venner?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s520_ridemoto',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… køre på motorcykel uden hjelm?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s521_choosecareer',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… vælge en karriere du virkelig føler for, i stedet for en mere sikker karriere?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s522_sayunpopularcase',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… sige hvad du mener om en upopulær sag til et møde på arbejdet?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s523_sunbathe',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… tage solbad uden solcreme?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s524_jumpbungee',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… springe bungy-jump fra en høj bro?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s525_takesmallplane',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… flyve en lille flyvemaskine?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s526_gohomealone',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… gå alene hjem om natten gennem et af byens farlige kvarterer?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s527_movetofarawaycity',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… flytte til en by langt væk fra din familie?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s528_startnewcareer',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name="… påbegynde en ny karriere midt i 30'erne?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='s529_leavekidathome',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… efterlade dine små børn alene hjemme, imens du løber et ærinde?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s52_camping',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… campere ude i vildmarken?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s530_keeppurse',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… beholde en pung du har fundet, som indeholder 1.000 kroner?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s531_movehouse',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… flytte til et hus, som ligger langs bredden af en flod:'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s532_sendkidtoschool',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… sende børn i skolen, imens DMI varsler om farligt vejr i dit område:'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s533_drivefloodedroad',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… køre på en oversvømmet vej.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s534_parkcar',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… parkere din bil i et udsat område, imens DMI varsler om farligt vejr i regionen.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s535_hiking',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… tage på vandreture, imens DMI varsler om farligt vejr i området.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s53_beghorseracing',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… satse en dagløn på hestevæddeløb?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s54_investfund',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… investere 10% af din årsløn i en pensionsfond?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s55_drinking',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… drikke store mængder alkohol ved et socialt arrangement?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s56_taxdeduction',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… angive et lidt for højt fradrag til SKAT?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s57_disagreeauth',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… erklære dig uenig med en autoritet, hvad angår et vigtigt emne?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s58_stakepokergame',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… satse en dagløn på et pokerspil med høje indsatser?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s59_affair',
            field=otree.db.models.StringField(choices=[['highly_unlikely', 'højst usandsynligt'], ['unlikely', 'usandsynligt'], ['not_certain', 'ikke sikkert'], ['likely', 'sandsynligt'], ['highly_likely', 'højst sandsynligt']], max_length=10000, null=True, verbose_name='… have en affære med en gift person?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s610_takecredit',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… tage æren for en anden persons arbejde?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s611_rundownski',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… køre ned ad en skiløjpe, der er vanskeligere end dine evner rækker til?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s612_invest5perincome',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… investere 5% af din årsindtægt i en stærkt spekulativ aktie?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s613_whitewaterrafting',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… tage på white water rafting om foråret når strømmen er stærkest?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s614_wageonmatch',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… satse en dagløn på en sportskamp (f.eks. fodbold, boksning eller håndbold)??'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s615_unsupportedsex',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… dyrke ubeskyttet sex?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s616_revealsecret',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… røbe en vens hemmelighed til en anden person?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s617_drivecarnobelt',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… køre i bil uden sele?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s618_investstartup',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… investere 10% af din årsindtægt i en nystartet virksomhed?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s619_learnparachute',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… lære at springe i faldskærm?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s61_diff_taste',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… indrømme, at du har en anderledes smag end dine venner?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s620_ridemoto',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… køre på motorcykel uden hjelm?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s621_choosecareer',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… vælge en karriere du virkelig føler for, i stedet for en mere sikker karriere?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s622_sayunpopularcase',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… sige hvad du mener om en upopulær sag til et møde på arbejdet?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s623_sunbathe',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… tage solbad uden solcreme?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s624_jumpbungee',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… springe bungy-jump fra en høj bro?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s625_takesmallplane',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… flyve en lille flyvemaskine?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s626_gohomealone',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… gå alene hjem om natten gennem et af byens farlige kvarterer?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s627_movetofarawaycity',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… flytte til en by langt væk fra din familie?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s628_startnewcareer',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name="… påbegynde en ny karriere midt i 30'erne?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='s629_leavekidathome',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… efterlade dine små børn alene hjemme, imens du løber et ærinde?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s62_camping',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… campere ude i vildmarken?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s630_keeppurse',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… beholde en pung du har fundet, som indeholder 1.000 kroner?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s631_movehouse',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… flytte til et hus beliggende langs bredden af en flod:'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s632_sendkidtoschool',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… sende børn i skolen, imens DMI varsler om farligt vejr i dit område:'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s633_drivefloodedroad',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… køre på en oversvømmet vej.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s634_parkcar',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… parkere din bil i et udsat område, imens DMI varsler om farligt vejr i regionen.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s635_hiking',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… tage på vandreture, imens DMI varsler om farligt vejr i området.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s63_beghorseracing',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… satse en dagløn på hestevæddeløb?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s64_investfund',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… investere 10% af din årsløn i en pensionsfond?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s65_drinking',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… drikke store mængder alkohol ved et socialt arrangement?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s66_taxdeduction',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… angive et lidt for højt fradrag til SKAT?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s67_disagreeauth',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… erklære dig uenig med en autoritet hvad angår et vigtigt emne?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s68_stakepokergame',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… satse en dagløn på et pokerspil med høje indsatser?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s69_affair',
            field=otree.db.models.StringField(choices=[['Not_risky_at_all', 'Slet ikke risikofyldt'], ['Very_little_risk', 'Meget lidt risiko'], ['No_risk', 'Nogen risiko'], ['High_risk', 'Høj risiko'], ['Very_high_risk', 'Allerhøjest risiko']], max_length=10000, null=True, verbose_name='… have en affære med en gift person?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s712_wondering',
            field=otree.db.models.StringField(choices=[['strongly_agree', 'meget enig'], ['agree', 'enig'], ['n_agree_disagree', 'hverken enig eller uenig'], ['disagree', 'uenig'], ['strongdisagree', 'meget uenig']], max_length=10000, null=True, verbose_name='Jeg gad godt vide, hvordan man på uærlig vis kan tjene en masse penge.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s724_soap',
            field=otree.db.models.StringField(choices=[['strongly_agree', 'meget enig'], ['agree', 'enig'], ['n_agree_disagree', 'hverken enig eller uenig'], ['disagree', 'uenig'], ['strongdisagree', 'meget uenig']], max_length=10000, null=True, verbose_name='Jeg har krav på særbehandling.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='s72_thingsinplace',
            field=otree.db.models.StringField(choices=[['strongly_agree', 'meget enig'], ['agree', 'enig'], ['n_agree_disagree', 'hverken enig eller uenig'], ['disagree', 'uenig'], ['strongdisagree', 'meget uenig']], max_length=10000, null=True, verbose_name='Jeg sørger for, at mine ting altid er på deres plads.'),
        ),
    ]
