from django.contrib import admin
from frontpage.models import * 

class OneAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
       num_objects = self.model.objects.count()
       if num_objects >= 1:
           return False
       else:
           return True

admin.site.register(HeaderPicture, OneAdmin)
admin.site.register(Background, OneAdmin)

admin.site.register(FrontPageCarousel, OneAdmin)
admin.site.register(RobotCarousel)
admin.site.register(RobotBottomCarousel)
admin.site.register(Picture)

admin.site.register(PageGroup)
admin.site.register(FrontPage)
admin.site.register(RobotPage)
admin.site.register(Page)


# Register your models here.
