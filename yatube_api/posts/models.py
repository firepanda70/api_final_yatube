import textwrap

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=200,
        help_text='Название группы'
    )
    slug = models.SlugField('Адрес', unique=True, help_text='Адрес группы')
    description = models.TextField('Описание', help_text='Описание группы')

    class Meta:
        verbose_name = 'Группа'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField('Текст', help_text='Текст поста')
    pub_date = models.DateTimeField(
        'Дата пуликации',
        auto_now_add=True,
        help_text='Дата публикации поста'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='posts',
        help_text='Автор поста'
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        help_text='Связанная группа'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        blank=True,
        null=True,
        help_text='Загрузите картинку',
    )

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Пост'

    def __str__(self):
        fullname = self.author.get_full_name()
        slug = self.author.username
        res = f'Автор: {fullname} ({slug})\n'
        res += f'Группа: {self.group}\n'
        res += f'Дата публикации: {self.pub_date.date()}\n'
        shorten_text = textwrap.shorten(
            text=self.text,
            width=20,
            placeholder='...'
        )
        res += f'Текст: {shorten_text}'
        return res


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name='Пост',
        related_name='comments',
        help_text='Комментируемый пост',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='comments',
        help_text='Автор комментария'
    )
    text = models.TextField('Текст', help_text='Текст комментария')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        help_text='Дата добавления комментария',
        db_index=True
    )

    class Meta():
        ordering = ('created', )
        verbose_name = 'Комментарий'

    def __str__(self):
        fullname = self.author.get_full_name()
        slug = self.author.username
        res = f'Автор: {fullname} ({slug})\n'
        res += f'Текст: {self.text}\n'
        res += self.created.strftime('%b %d, %Y, %H:%M')
        return res

class Follow(models.Model):
    origin = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
        related_name='follower',
        help_text='Подписчик пользователя'
    )
    target = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='following',
        help_text='Автор'
    )

    class Meta():
        ordering = ('target', )
        verbose_name = 'Подписческа'
        unique_together = ('origin', 'target',)

    def __str__(self):
        return (f'Подписка {self.origin.get_full_name()} '
                f'({self.origin.username}) на {self.target.get_full_name()} '
                f'({self.target.username})')