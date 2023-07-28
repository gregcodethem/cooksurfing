import sys
import os
cwd = os.getcwd()
INTERP = "/home/cooklucida/.local/share/virtualenvs/cooking.medialucida.co.uk-Rg0-2_cj"
# INTERP is present twice so that the new python interpreter
# knows the actual executable path
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/lucidcooking')  # You must add your project here

sys.path.insert(0, '/home/cooklucida/.local/share/virtualenvs/cooking.medialucida.co.uk-Rg0-2_cj')
sys.path.insert(
    0, cwd + '/home/cooklucida/.local/share/virtualenvs/cooking.medialucida.co.uk-Rg0-2_cj/lib/python3.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "config.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
