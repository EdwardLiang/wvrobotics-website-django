from django.contrib import admin
from frontpage.models import * 

admin.site.register(Picture)
admin.site.register(Carousel)
admin.site.register(Page)
admin.site.register(RobotPage)
admin.site.register(PageGroup)


class OneAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
       num_objects = self.model.objects.count()
       if num_objects >= 1:
           return False
       else:
           return True

admin.site.register(Background, OneAdmin)
admin.site.register(HeaderPicture, OneAdmin)
# Register your models here.
