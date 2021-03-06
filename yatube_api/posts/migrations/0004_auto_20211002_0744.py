# Generated by Django 2.2.16 on 2021-10-02 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20211002_0504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ('following',), 'verbose_name': 'Подписческа'},
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='target',
            new_name='following',
        ),
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(default=1, help_text='Подписчик автора', on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Подписчик'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user', 'following')},
        ),
        migrations.RemoveField(
            model_name='follow',
            name='origin',
        ),
    ]
