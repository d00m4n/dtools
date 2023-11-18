"""
    Show program banner
"""
# Importaciones de módulos estándar
from os import path
from inspect import stack
# Importaciones de módulos externos
from pyfiglet import Figlet # SHOW TEXT BANNER

# Importaciones personalizadas
from dtools import script_name
def show_banner(stext=None,font_name='graffiti',version=""):
    """
    Shows script banner
    """
    if stext is None:
        filename = stack()[1].filename 
        stext=path.basename(filename).split(".")[0].upper()
    print(colorme.GREEN)
    f = Figlet(font=font_name)
    banner=f.renderText(stext)
    print(banner)
    print(__version__)
    print(colorme.ENDC)

if __name__ == "__main__":
    from colorme import colorme
    
    show_banner(script_name().upper())
    exit()

from dtools.colorme import colorme
