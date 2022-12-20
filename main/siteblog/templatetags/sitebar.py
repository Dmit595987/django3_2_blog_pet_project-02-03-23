from django import template
from siteblog.models import Tag, Post

register = template.Library()

@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular_posts(cnt=5):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}

