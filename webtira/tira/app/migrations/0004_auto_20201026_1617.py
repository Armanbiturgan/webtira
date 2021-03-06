# Generated by Django 3.0.5 on 2020-10-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_person_married'),
    ]

    operations = [
        migrations.CreateModel(
            name='np',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oblast', models.CharField(max_length=100, verbose_name='full name')),
                ('region', models.CharField(max_length=100, verbose_name='full name')),
                ('snp', models.CharField(max_length=100, verbose_name='full name')),
                ('popul', models.CharField(max_length=100, verbose_name='full name')),
                ('evdo', models.CharField(max_length=100, verbose_name='full name')),
                ('adsl', models.CharField(max_length=100, verbose_name='full name')),
                ('ftthb', models.CharField(max_length=100, verbose_name='full name')),
                ('satellite', models.CharField(max_length=100, verbose_name='full name')),
                ('twog', models.CharField(max_length=100, verbose_name='full name')),
                ('threeg', models.CharField(max_length=100, verbose_name='full name')),
                ('fourg', models.CharField(max_length=100, verbose_name='full name')),
                ('vols', models.CharField(max_length=100, verbose_name='full name')),
                ('lte', models.CharField(max_length=100, verbose_name='full name')),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='organization',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
