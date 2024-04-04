# Generated by Django 3.2.5 on 2024-04-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('serielno', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=20)),
                ('authorname', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=10)),
            ],
        ),
    ]
