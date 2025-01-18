from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Users, Posts, Comments, Albums, Photos, Todos

admin.site.register(Users)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Albums)
admin.site.register(Photos)
admin.site.register(Todos)