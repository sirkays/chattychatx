# Generated by Django 4.1.1 on 2022-10-06 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_chatboxdata_my_image_chatboxdata_other_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('chat_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='chat.chatboxdata')),
            ],
        ),
    ]
