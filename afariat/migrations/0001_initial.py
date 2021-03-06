# Generated by Django 4.0.3 on 2022-06-17 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CategorieAnnonce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterielleInformatique',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nameMatrInformatique', models.CharField(max_length=255)),
                ('imageMatrInformatique', models.TextField(blank=True, db_column='data', null=True)),
                ('priceMatrInformatique', models.CharField(max_length=255, null=True)),
                ('dateMatrInformatique', models.CharField(max_length=255, null=True)),
                ('annoceMatrInformatique', models.CharField(max_length=255, null=True)),
                ('villeMatrInformatique', models.CharField(max_length=255, null=True)),
                ('annoceWNScrappOfAdmin', models.BooleanField(default=False)),
                ('activationAnnonce', models.BooleanField(default=False)),
                ('emailUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
                ('idMaterielleInformatique', models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='CategorieAnnonce.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Immobilier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nameImmobilier', models.CharField(max_length=255)),
                ('imageImmobilier', models.TextField(blank=True, db_column='data', null=True)),
                ('priceImmobilier', models.CharField(max_length=255, null=True)),
                ('dateImmobilier', models.CharField(max_length=255, null=True)),
                ('annoceImmobilier', models.CharField(max_length=255, null=True)),
                ('villeImmobilier', models.CharField(max_length=255, null=True)),
                ('activationAnnonce', models.BooleanField(default=False)),
                ('annoceWNScrappOfAdmin', models.BooleanField(default=False)),
                ('emailUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
                ('idImmobilier', models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='CategorieAnnonce.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Emploi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nameEmploi', models.CharField(max_length=255)),
                ('imageEmploi', models.TextField(blank=True, db_column='data', null=True)),
                ('priceEmploi', models.CharField(max_length=255, null=True)),
                ('dateEmploi', models.CharField(max_length=255, null=True)),
                ('annoceEmploi', models.CharField(max_length=255, null=True)),
                ('villeEmploi', models.CharField(max_length=255, null=True)),
                ('activationAnnonce', models.BooleanField(default=False)),
                ('annoceWNScrappOfAdmin', models.BooleanField(default=False)),
                ('emailUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
                ('idEmploi', models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='CategorieAnnonce.categorie')),
            ],
        ),
    ]
