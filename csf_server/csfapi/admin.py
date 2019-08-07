from django.contrib import admin

from . models import Issues, Users, Clients, ClientGroups

# Register your models here.

admin.site.register(Issues)
admin.site.register(Users)
admin.site.register(Clients)
admin.site.register(ClientGroups)

