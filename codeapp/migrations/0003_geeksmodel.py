# Generated by Django 3.1.1 on 2021-01-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeapp', '0002_auto_20210105_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
