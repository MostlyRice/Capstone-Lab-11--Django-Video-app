# Generated by Django 3.1.2 on 2023-04-25 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_id',
            field=models.CharField(default=1, max_length=40, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
