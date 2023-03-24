from django.contrib import admin
from django.urls import path, include
from classroom.views import index
from django.conf import settings
from django.conf.urls.static import static
from authy.views import UserProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("authy.urls")),
    path('course/', include("classroom.urls")),
    path('direct/', include("direct.urls")),
    path('', index, name='index'),
    path('<username>', UserProfile, name="user-profile"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ax.pie(sizes_console[angles_console[i]], colors=[colors_console[c] for c in consoles_company[angles_console[i]]],  startangle=angle1,  wedgeprops={'width': 0.5, 'edgecolor': 'white', 'linewidth': 1.5, 'edgecolor': 'white'},  counterclock=False,  radius=1.2,  center=(0, 0),  frame=True,  labeldistance=1.05,  textprops={'fontsize': 8, 'color': 'black', 'weight': 'bold'}, wedgeprops=dict(width=0.5, edgecolor='white'))