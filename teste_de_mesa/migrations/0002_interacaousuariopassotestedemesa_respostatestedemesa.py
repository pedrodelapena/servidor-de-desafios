# Generated by Django 3.0.2 on 2020-02-07 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('teste_de_mesa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RespostaTesteDeMesa',
            fields=[
                ('respostasubmetida_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.RespostaSubmetida')),
                ('resultado_linha', models.CharField(blank=True, choices=[('ER', 'Erro'), ('OK', 'OK')], max_length=2)),
                ('resultado_memoria', models.CharField(blank=True, choices=[('ER', 'Erro'), ('OK', 'OK')], max_length=2)),
                ('resultado_terminal', models.CharField(blank=True, choices=[('ER', 'Erro'), ('OK', 'OK')], max_length=2)),
                ('passo', models.IntegerField()),
                ('proxima_linha', models.IntegerField(default=-1)),
                ('memoria_str', models.TextField(blank=True)),
                ('terminal_str', models.TextField(blank=True)),
            ],
            bases=('core.respostasubmetida',),
        ),
        migrations.CreateModel(
            name='InteracaoUsuarioPassoTesteDeMesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passo', models.IntegerField()),
                ('tentativas', models.IntegerField(default=0)),
                ('melhor_resultado', models.CharField(choices=[('ER', 'Erro'), ('OK', 'OK')], default='ER', max_length=2)),
                ('interacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.InteracaoUsarioExercicio')),
                ('ultima_submissao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.RespostaSubmetida')),
            ],
            options={
                'unique_together': {('interacao', 'passo')},
            },
        ),
    ]
