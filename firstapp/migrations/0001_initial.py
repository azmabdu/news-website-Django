# Generated by Django 4.0.4 on 2022-07-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_photo', models.FileField(upload_to='firstapp/static/media')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('section', models.CharField(choices=[('Политика', 'Политика'), ('Экономика', 'Экономика'), ('Общество', 'Общество'), ('Культура', 'Культура'), ('Спорт', 'Спорт'), ('В мире', 'В мире')], max_length=100)),
                ('tags', models.CharField(max_length=100)),
            ],
        ),
    ]
