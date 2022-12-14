# Generated by Django 4.1.2 on 2022-10-28 23:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=2000, verbose_name='コメント')),
            ],
        ),
        migrations.CreateModel(
            name='TopicImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('image', models.ImageField(upload_to='testapp/topic_image/comment', verbose_name='画像')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.topic', verbose_name='トピック')),
            ],
        ),
    ]
