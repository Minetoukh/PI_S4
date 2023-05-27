# Generated by Django 4.1.3 on 2023-05-26 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Encadrent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('numero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Encdprof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('numero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Entre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Etud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.IntegerField(max_length=40)),
                ('Nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=40)),
                ('Dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_stages.dep')),
            ],
        ),
        migrations.CreateModel(
            name='grp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=50)),
                ('membres', models.CharField(max_length=50)),
                ('idEtud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_stages.etud')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Simester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Type_Encadrant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Type_stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('dattedebut', models.DateField(max_length=50)),
                ('dattefin', models.DateField(max_length=50)),
                ('datesoutenance', models.DateField(max_length=50)),
                ('lieu', models.CharField(max_length=50)),
                ('Annee', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('grp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_stages.grp')),
            ],
        ),
        migrations.AddField(
            model_name='grp',
            name='idSimester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_stages.simester'),
        ),
        migrations.CreateModel(
            name='Encadrer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Encadrent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_stages.encadrent')),
                ('Stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_stages.stage')),
            ],
        ),
        migrations.CreateModel(
            name='contenir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_stages.dep')),
                ('grp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='G_stages.grp')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='grp',
            unique_together={('idSimester', 'idEtud')},
        ),
    ]
