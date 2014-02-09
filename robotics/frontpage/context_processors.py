# context_processors.py
from frontpage.models import * 

def base(request):

    if HeaderPicture.objects.all(): 
        header_picture = HeaderPicture.objects.all()[0]
    else:
        header_picture = None
    if Background.objects.all():
        background = Background.objects.all()[0]
    else:
        background = None
    page_groups = PageGroup.objects.all()
    return {
        'header_picture' : header_picture,
        'page_groups' : page_groups,
        'background' : background,
    }
