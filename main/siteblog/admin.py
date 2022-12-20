from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Tag, Category, Post
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())


    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    prepopulated_fields = {'slug': ('title', )}
    form = PostAdminForm
    list_display = ('id', 'title', 'views', 'author', 'slug', 'category','created_at', 'get_photo')
    list_display_links = ('id', 'title', 'author', 'slug', 'category',)
    search_fields = ('id', 'title',)
    list_filter = ('title', 'tags',)
    readonly_fields = ('views', 'created_at')


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="30">')
        return '-'

    get_photo.short_description = 'Photo'



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)



