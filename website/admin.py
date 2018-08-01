from django.contrib import admin
from bridges.website.models import *

class MiscPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'priority')
    list_editable = ('active', 'priority')
    
    prepopulated_fields = {'slug':('name',)}
    class Media:
        js = ['/media/adminmedia/tinymce/jscripts/tiny_mce/tiny_mce.js', '/media/adminmedia/tinymce_setup/tinymce_setup.js',]

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority')
    list_editable = ('priority',)
    class Media:
        js = ['/media/adminmedia/tinymce/jscripts/tiny_mce/tiny_mce.js', '/media/adminmedia/tinymce_setup/tinymce_setup.js',]

class SiteMetaInline(admin.StackedInline):
    model = SiteMeta
    class Media:
        js = ['/media/adminmedia/tinymce/jscripts/tiny_mce/tiny_mce.js', '/media/adminmedia/tinymce_setup/tinymce_setup.js',]

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('email','firstname', 'lastname', 'comment')
    list_filter = ('subscribe',)

admin.site.register(MiscPage, MiscPageAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Service)
admin.site.register(ImageSlider)

from django.contrib.sites.admin import SiteAdmin

admin.site.unregister(Site)

class MySiteAdmin(SiteAdmin):
    model = Site
    list_display = ('domain','name')
    inlines = [SiteMetaInline,]
    
admin.site.register(Site, MySiteAdmin)


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
class MyUserAdmin(UserAdmin):
    staff_fieldsets = (
        (None, {'fields': ('username',)}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'),{'fields':('is_active','is_staff')}),
        #(('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Groups'), {'fields': ('groups',)}),
    )

    def change_view(self, request, *args, **kwargs):
        # for non-superuser
        if not request.user.is_superuser:
            try:
                self.fieldsets = self.staff_fieldsets
                response = UserAdmin.change_view(self, request, *args, **kwargs)
            finally:
                # Reset fieldsets to its original value
                self.fieldsets = UserAdmin.fieldsets
            return response
        else:
            return UserAdmin.change_view(self, request, *args, **kwargs)
    
    def queryset(self, request):
        #form.status.queryset = OrderStatus.objects.exclude(status="In Progress")
        if not request.user.is_superuser:
            return super(UserAdmin,self).queryset(request).exclude(is_superuser=True) 
        else:
            return super(UserAdmin,self).queryset(request)
           
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)