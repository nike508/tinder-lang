from django.contrib import admin

from .models import Group, Profile, Match, Comment, Language, UserLanguage, Unmatch

admin.site.register(Group)
admin.site.register(Profile)
admin.site.register(Match)
admin.site.register(Comment)
admin.site.register(Language)
admin.site.register(UserLanguage)
admin.site.register(Unmatch)
# Register your models here.
