from django.contrib import admin
from .models import Account, User, Role, Color, Skill

# Register your models here.

admin.site.register(Account);
admin.site.register(User);
admin.site.register(Role);
admin.site.register(Skill);
admin.site.register(Color);