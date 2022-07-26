# Generated by Django 4.0.4 on 2022-07-23 11:26

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0009_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('profile_pictire', models.ImageField(upload_to='images/profile_picture')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('country_origin', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.user'),
            preserve_default=False,
        ),
    ]
