from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as userAdmin
from users.models import Profiles
from django.contrib.auth.models import User
#admin.site.register(Profiles)

@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    #campos que muestro en la grilla ya creados
    list_display = ('pk','website', 'picture','bio')
    list_display_links = ('website', 'picture')

    #list_editable = ('website', 'picture')

    search_fields = (
                    'website',
                    'picture'
                    #busca por todos los campos
                    )

    list_filter = ('website', )

    #group fields when create profile (user from user each user one profile)
    fieldsets = (
        ('Profile',{
        'fields':(('user','website','picture'),),
        }),
        ('Aditional Info', {
        'fields': (('bio',),),
        })
    )

#vincular modelos para registrar (es decir cuando creo un user creo un profile to do a la vez)
class ProfileInline(admin.StackedInline):
        model = Profiles
        can_delete = False
        verbose_name_plural ='users'


class UserAdmin (userAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)