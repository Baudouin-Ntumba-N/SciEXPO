# Generated by Django 4.1.7 on 2023-08-09 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='inscrit',
            name='function_in_school',
            field=models.CharField(choices=[('Eleve', 'Elève'), ('Professeur', 'Professeur'), ('-', '-')], default='-', max_length=20, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='inscrit',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='option',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
