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
from dtools import cfgRead
def show_banner(banner_text=None,font_name='graffiti',version="",by_name="by dr_d00m4n"):
    """
    Shows script banner
    """
    if banner_text is None:
        filename = stack()[1].filename
        folder_path=path.dirname(filename)
        banner_text=path.basename(filename).split(".")[0].upper()

    try:
        version=cfgRead(f"{folder_path}/version.py")["__version__"]
        
    except:
        version=""

    name_len=len(by_name)
    print(colorme.GREEN)
    f = Figlet(font=font_name)
    banner=f.renderText(banner_text)
    tab=int((len(banner)/6)-name_len)-len(version)
    print(banner)
    print(version.replace("'","")+" "*tab+by_name)
    print(colorme.ENDC)

if __name__ == "__main__":
    from colorme import colorme
    
    show_banner()
    exit()

from dtools.colorme import colorme
