from django.contrib import admin

# Register your models here.
from fc_user.models import FcUser


class FcUserAdmin(admin.ModelAdmin):
    list_display = ('email', )


admin.site.register(FcUser, FcUserAdmin)
