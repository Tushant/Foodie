from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from userprofiles.models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(get_user_model()) # because its(User) not always guranteed that user is the User model
admin.site.register(get_user_model(), UserAdmin)