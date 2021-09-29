from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class AdminZonePost(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Group)
class AdminZoneGroup(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description',)
    list_filter = ('title',)


@admin.register(Comment)
class AdminZoneComment(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'post', 'created',)
    list_filter = ('post',)


@admin.register(Follow)
class AdminZoneFollow(admin.ModelAdmin):
    list_display = ('pk', 'origin', 'target',)
    list_filter = ('origin', 'target', )
