from django.contrib import admin

from .models import Group, Profile, Match, Comment

admin.site.register(Group)
admin.site.register(Profile)
admin.site.register(Match)
admin.site.register(Comment)
# Register your models here.
