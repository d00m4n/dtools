# ------------------------------| Classes
class color:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def setcolor(text, color="white"):   
    colors= {"purple":'\033[95m',"blue" : '\033[94m',"green" : '\033[92m' ,"yellow" : '\033[93m',"red" : '\033[91m',"white" : '\033[0m',"cyan" : '\033[96m',"grey" : '\033[38;5;238m',"orange" : '\033[38;5;214m'}#,BOLD = '\033[1m',UNDERLINE = '\033[4m'}
    return (colors[color.lower()]+text+colors["white"])

def tabout(
    text,value="",separator=":",
    textcolor="white",
    valuecolor="cyan",
    head="",
    headcolor="white",
    textsize=8,
    skin="",
    ident=0,
    autosize=False    
    ):
    ident=" "*ident
    final_text=text
    spaces=(textsize - len(text)-len(ident))
    if spaces < 0 and not skin:
        final_text=text[0:textsize-2]+".."
    if skin.lower()=="error":
        textcolor="red"
        valuecolor="red"
        headcolor="red"
        separator="\b"
        spaces=0
        
    if skin.lower()=="warning":
        textcolor="yellow"
        valuecolor="yellow"
        separator=""
    if head != "": 
        head+=" "
        spaces-=len(head)   
    if value=="" or autosize: 
        separator=""
        final_text=text

     

    print(ident+setcolor(head,headcolor.lower())+setcolor(final_text,textcolor.lower())+" "*spaces,separator,setcolor(str(value),valuecolor.lower())+color.ENDC)

# tabout("Closed",textcolor="green",textsize=14,head="·",ident=2)