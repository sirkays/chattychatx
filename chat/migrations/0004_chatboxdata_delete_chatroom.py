# Generated by Django 4.1.1 on 2022-10-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_chatroom_title_chatroom_room_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBoxData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=2500)),
                ('status', models.BooleanField(default=True)),
                ('user1', models.CharField(max_length=250)),
                ('user2', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
    ]
