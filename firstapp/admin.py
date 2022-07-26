from django.contrib import admin
from .models import Publication, Comment, User, Subcomment

admin.site.register(Publication)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Subcomment)
