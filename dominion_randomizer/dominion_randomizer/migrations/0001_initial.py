# Generated by Django 2.1.1 on 2020-01-28 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_jp_kanji', models.CharField(max_length=30)),
                ('name_jp_pronunciations', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=60)),
                ('text_jp', models.TextField()),
                ('text_en', models.TextField()),
            ],
            options={
                'db_table': 'artifacts',
            },
        ),
        migrations.CreateModel(
            name='BaseCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_jp_kanji', models.CharField(max_length=30)),
                ('name_jp_pronunciations', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=60)),
                ('text_jp', models.TextField()),
                ('text_en', models.TextField()),
                ('cost_coin', models.IntegerField(null=True)),
                ('cost_potion', models.IntegerField(null=True)),
                ('cost_debt', models.IntegerField(null=True)),
                ('gain_card', models.IntegerField(null=True)),
                ('gain_action', models.IntegerField(null=True)),
                ('gain_buy', models.IntegerField(null=True)),
                ('gain_coin', models.IntegerField(null=True)),
                ('gain_vp', models.IntegerField(null=True)),
                ('gain_villager', models.IntegerField(null=True)),
                ('gain_coffer', models.IntegerField(null=True)),
                ('types', models.CharField(max_length=60)),
                ('action', models.BooleanField(default=False, null=True)),
                ('attack', models.BooleanField(default=False, null=True)),
                ('castle', models.BooleanField(default=False, null=True)),
                ('curse', models.BooleanField(default=False, null=True)),
                ('doom', models.BooleanField(default=False, null=True)),
                ('duration', models.BooleanField(default=False, null=True)),
                ('fate', models.BooleanField(default=False, null=True)),
                ('gathering', models.BooleanField(default=False, null=True)),
                ('heirloom', models.BooleanField(default=False, null=True)),
                ('knight', models.BooleanField(default=False, null=True)),
                ('night', models.BooleanField(default=False, null=True)),
                ('looter', models.BooleanField(default=False, null=True)),
                ('prize', models.BooleanField(default=False, null=True)),
                ('reaction', models.BooleanField(default=False, null=True)),
                ('reserve', models.BooleanField(default=False, null=True)),
                ('ruins', models.BooleanField(default=False, null=True)),
                ('spirit', models.BooleanField(default=False, null=True)),
                ('shelter', models.BooleanField(default=False, null=True)),
                ('treasure', models.BooleanField(default=False, null=True)),
                ('traveller', models.BooleanField(default=False, null=True)),
                ('victory', models.BooleanField(default=False, null=True)),
                ('zombie', models.BooleanField(default=False, null=True)),
            ],
            options={
                'db_table': 'base_cards',
            },
        ),
        migrations.CreateModel(
            name='Boon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_jp_kanji', models.CharField(max_length=30)),
                ('name_jp_pronunciations', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=60)),
                ('text_jp', models.TextField()),
                ('text_en', models.TextField()),
            ],
            options={
                'db_table': 'boons',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_jp_kanji', models.CharField(max_length=30)),
                ('name_jp_pronunciations', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=60)),
                ('text_jp', models.TextField()),
                ('text_en', models.TextField()),
                ('cost_coin', models.IntegerField(null=True)),
                ('cost_potion', models.IntegerField(null=True)),
                ('cost_debt', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='Expansion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_jp_kanji', models.CharField(max_length=30)),
                ('name_jp_pronunciations', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'expansions',
            },
        ),
        migrations.CreateModel(
            name='Hex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_jp_kanji', models.CharField(max_length=30)),
                ('name_jp_pronunciations', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=60)),
                ('text_jp', models.TextField()),
                ('text_en', models.TextField()),
                ('expansion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dominion_randomizer.Expansion')),
            ],
            options={
                'db_table': 'hexes',
            },
        ),
        migrations.CreateModel(
            name='KingdomCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_jp_kanji', models.CharField(max_length=30)),
                ('name_jp_pronunciations', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=60)),
                ('text_jp', models.TextField()),
                ('text_en', models.TextField()),
                ('cost_coin', models.IntegerField(null=True)),
                ('cost_potion', models.IntegerField(null=True)),
                ('cost_debt', models.IntegerField(null=True)),
                ('gain_card', models.IntegerField(null=True)),
                ('gain_action', models.IntegerField(null=True)),
                ('gain_buy', models.IntegerField(null=True)),
                ('gain_coin', models.IntegerField(null=True)),
                ('gain_vp', models.IntegerField(null=True)),
                ('gain_villager', models.IntegerField(null=True)),
                ('gain_coffer', models.IntegerField(null=True)),
                ('types', models.CharField(max_length=60)),
                ('action', models.BooleanField(default=False, null=True)),
                ('attack', models.BooleanField(default=False, null=True)),
                ('castle', models.BooleanField(default=False, null=True)),
                ('curse', models.BooleanField(default=False, null=True)),
                ('doom', models.BooleanField(default=False, null=True)),
                ('duration', models.BooleanField(default=False, null=True)),
                ('fate', models.BooleanField(default=False, null=True)),
                ('gathering', models.BooleanField(default=False, null=True)),
                ('heirloom', models.BooleanField(default=False, null=True)),
                ('knight', models.BooleanField(default=False, null=True)),
                ('night', models.BooleanField(default=False, null=True)),
                ('looter', models.BooleanField(default=False, null=True)),
                ('prize', models.BooleanField(default=False, null=True)),
                ('reaction', models.BooleanField(default=False, null=True)),
                ('reserve', models.BooleanField(default=False, null=True)),
                ('ruins', models.BooleanField(default=False, null=True)),
                ('spirit', models.BooleanField(default=False, null=True)),
                ('shelter', models.BooleanField(default=False, null=True)),
                ('treasure', models.BooleanField(default=False, null=True)),
                ('traveller', models.BooleanField(default=False, null=True)),
                ('victory', models.BooleanField(default=False, null=True)),
                ('zombie', models.BooleanField(default=False, null=True)),
                ('expansion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dominion_randomizer.Expansion')),
            ],
            options={
                'db_table': 'kingdom_cards',
            },
        ),
        migrations.CreateModel(
            name='Landmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_jp_kanji', models.CharField(max_length=30)),
                ('name_jp_pronunciations', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=60)),
                ('text_jp', models.TextField()),
                ('text_en', models.TextField()),
                ('expansion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dominion_randomizer.Expansion')),
            ],
            options={
                'db_table': 'landmarks',
            },
        ),
        migrations.CreateModel(
            name='NonSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_jp_kanji', models.CharField(max_length=30)),
                ('name_jp_pronunciations', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=60)),
                ('text_jp', models.TextField()),
                ('text_en', models.TextField()),
                ('cost_coin', models.IntegerField(null=True)),
                ('cost_potion', models.IntegerField(null=True)),
                ('cost_debt', models.IntegerField(null=True)),
                ('gain_card', models.IntegerField(null=True)),
                ('gain_action', models.IntegerField(null=True)),
                ('gain_buy', models.IntegerField(null=True)),
                ('gain_coin', models.IntegerField(null=True)),
                ('gain_vp', models.IntegerField(null=True)),
                ('gain_villager', models.IntegerField(null=True)),
                ('gain_coffer', models.IntegerField(null=True)),
                ('types', models.CharField(max_length=60)),
                ('action', models.BooleanField(default=False, null=True)),
                ('attack', models.BooleanField(default=False, null=True)),
                ('castle', models.BooleanField(default=False, null=True)),
                ('curse', models.BooleanField(default=False, null=True)),
                ('doom', models.BooleanField(default=False, null=True)),
                ('duration', models.BooleanField(default=False, null=True)),
                ('fate', models.BooleanField(default=False, null=True)),
                ('gathering', models.BooleanField(default=False, null=True)),
                ('heirloom', models.BooleanField(default=False, null=True)),
                ('knight', models.BooleanField(default=False, null=True)),
                ('night', models.BooleanField(default=False, null=True)),
                ('looter', models.BooleanField(default=False, null=True)),
                ('prize', models.BooleanField(default=False, null=True)),
                ('reaction', models.BooleanField(default=False, null=True)),
                ('reserve', models.BooleanField(default=False, null=True)),
                ('ruins', models.BooleanField(default=False, null=True)),
                ('spirit', models.BooleanField(default=False, null=True)),
                ('shelter', models.BooleanField(default=False, null=True)),
                ('treasure', models.BooleanField(default=False, null=True)),
                ('traveller', models.BooleanField(default=False, null=True)),
                ('victory', models.BooleanField(default=False, null=True)),
                ('zombie', models.BooleanField(default=False, null=True)),
                ('expansion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dominion_randomizer.Expansion')),
            ],
            options={
                'db_table': 'non_supplies',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_jp_kanji', models.CharField(max_length=30)),
                ('name_jp_pronunciations', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=60)),
                ('text_jp', models.TextField()),
                ('text_en', models.TextField()),
                ('expansion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dominion_randomizer.Expansion')),
            ],
            options={
                'db_table': 'projects',
            },
        ),
        migrations.CreateModel(
            name='RandomizerCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_jp_kanji', models.CharField(max_length=30)),
                ('name_jp_pronunciations', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=60)),
                ('text_jp', models.TextField()),
                ('text_en', models.TextField()),
                ('cost_coin', models.IntegerField(null=True)),
                ('cost_potion', models.IntegerField(null=True)),
                ('cost_debt', models.IntegerField(null=True)),
                ('gain_card', models.IntegerField(null=True)),
                ('gain_action', models.IntegerField(null=True)),
                ('gain_buy', models.IntegerField(null=True)),
                ('gain_coin', models.IntegerField(null=True)),
                ('gain_vp', models.IntegerField(null=True)),
                ('gain_villager', models.IntegerField(null=True)),
                ('gain_coffer', models.IntegerField(null=True)),
                ('types', models.CharField(max_length=60)),
                ('action', models.BooleanField(default=False, null=True)),
                ('attack', models.BooleanField(default=False, null=True)),
                ('castle', models.BooleanField(default=False, null=True)),
                ('curse', models.BooleanField(default=False, null=True)),
                ('doom', models.BooleanField(default=False, null=True)),
                ('duration', models.BooleanField(default=False, null=True)),
                ('fate', models.BooleanField(default=False, null=True)),
                ('gathering', models.BooleanField(default=False, null=True)),
                ('heirloom', models.BooleanField(default=False, null=True)),
                ('knight', models.BooleanField(default=False, null=True)),
                ('night', models.BooleanField(default=False, null=True)),
                ('looter', models.BooleanField(default=False, null=True)),
                ('prize', models.BooleanField(default=False, null=True)),
                ('reaction', models.BooleanField(default=False, null=True)),
                ('reserve', models.BooleanField(default=False, null=True)),
                ('ruins', models.BooleanField(default=False, null=True)),
                ('spirit', models.BooleanField(default=False, null=True)),
                ('shelter', models.BooleanField(default=False, null=True)),
                ('treasure', models.BooleanField(default=False, null=True)),
                ('traveller', models.BooleanField(default=False, null=True)),
                ('victory', models.BooleanField(default=False, null=True)),
                ('zombie', models.BooleanField(default=False, null=True)),
                ('expansion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dominion_randomizer.Expansion')),
            ],
            options={
                'db_table': 'randomizer_cards',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_jp_kanji', models.CharField(max_length=30)),
                ('name_jp_pronunciations', models.CharField(max_length=30)),
                ('name_en', models.CharField(max_length=60)),
                ('text_jp', models.TextField()),
                ('text_en', models.TextField()),
                ('expansion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dominion_randomizer.Expansion')),
            ],
            options={
                'db_table': 'states',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='expansion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dominion_randomizer.Expansion'),
        ),
        migrations.AddField(
            model_name='boon',
            name='expansion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dominion_randomizer.Expansion'),
        ),
        migrations.AddField(
            model_name='basecard',
            name='expansion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dominion_randomizer.Expansion'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='expansion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dominion_randomizer.Expansion'),
        ),
    ]
