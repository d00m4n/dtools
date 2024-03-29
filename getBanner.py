"""
Show banner
"""

import sys
from dtools import setcolor

def getBanner(
    text,
    lines=50,
    spacer="-",
    preTxt="[",
    postTxt="]",
    head="",
    end="",
    textColor="white",
    spaces=True
    ): #print a banner


    spacesLen=0
    space=""
    textLen=len(text)
    preTxtLen=len(preTxt)
    headLen=len(head)
    endLen=len(end)
    if spaces:
       spacesLen=2
       space=" "
    preLines=int((lines - textLen -preTxtLen -spacesLen - headLen - endLen)/2)
    line=head+spacer*preLines + preTxt + space + setcolor(text,textColor)+ space + postTxt + spacer*preLines+end
    print()
    print(line)
    print()


if __name__ == "__main__":
    getBanner("D00m4n",preTxt="|",postTxt="|",head=">",end="<",textColor="grey")
    sys.exit()
