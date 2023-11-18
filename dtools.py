import time
import random
import sys
import os
import base64
import zlib
import datetime
import inspect #used for scriptname function
from platform import system as OS # needed for clear_host function
def clear_host():
    """
    clean screen based on system
    """
    print( OS() == "Windows")
    if OS() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

class color: # colorize text
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[96m'
    ORANGE = '\033[38;5;214m'
    GREY = '\033[38;5;238m'

    def num(value):
        return f'\033[38;5;{value}m'

def script_name() -> str:
    """
    return script name
    """
    # Return scripts name
    filename = inspect.stack()[1].filename 
    return os.path.basename(filename).split(".")[0]

def setcolor(text, color="white"):   
    colors= {"purple":'\033[95m',"blue" : '\033[94m',"green" : '\033[92m' ,"yellow" : '\033[93m',"red" : '\033[91m',"white" : '\033[0m',"cyan" : '\033[96m',"grey" : '\033[38;5;238m',"orange" : '\033[38;5;214m'}#,BOLD = '\033[1m',UNDERLINE = '\033[4m'}
    return (colors[color.lower()]+text+colors["white"])

# color reference
# def colors_256(color_):
#     num1 = str(color_)
#     num2 = str(color_).ljust(3, ' ')
#     if color_ % 16 == 0:
#         return(f"\033[38;5;{num1}m {num2} \033[0;0m\n")
#     else:
#         return(f"\033[38;5;{num1}m {num2} \033[0;0m")
# convert epoc date to a human readeable value
def epochToHuman(epochdate):
    from datetime import datetime
    epochdate = int(str(epochdate)[0:10])  # remove milliseconds
    try:
        returnValue = datetime.fromtimestamp(int(epochdate))
    except Exception as errorEx:
        # print(f'{errorEx} ({epochdate})')
        exit()
    return returnValue

#generate md5 hash
def md5(fname):
    import hashlib
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def getWeekNumber(date=datetime.date.today()):
    return date.isocalendar()[1]

def getDayNumber(date=datetime.date.today()):
    return date.isocalendar()[2]

def getYearNumber(date=datetime.date.today()):
    return date.isocalendar()[0]

def nowDate():
    return datetime.date.today() 

def loadFile(file,format="raw"): 
    import json
    try:
        # log.debug(f"Loading {file}.")   
        text_file = open(file, "r", encoding="utf-8")     
        if format == "json":
            lines = json.load(text_file)            
        else:            
            lines = text_file.read().splitlines()
        # log.debug(f'{len(lines)} lines.')
    except Exception as errorEx :
        showError(errorEx)
        # log.warning(f"{file} don't exists.")
        return False
    return lines

def cfgRead(file):
    llista = loadFile(file)
    if llista:
        returnValue = {}
        for op in llista:
            if op[0] == "#":
                continue
            tmp = op.split("=")
            returnValue.update({tmp[0].strip() : tmp[1].strip()})
        return returnValue
    return False

def cfgSave(file,dicc):
    returnList = []
    for line in sorted(dicc):
        returnList.append(f"{line}={dicc[line]}")
    saveFile(file,returnList)

def saveFile(file,text,raw=False,type="w"):
    with open(file, type) as txt_file:
        if raw:
            txt_file.write(str(text))
        else :
            for line in text:                
                line = line.encode('ascii', 'ignore').decode("utf-8")
                txt_file.write(line + "\n") # works with any number of elements in a line

def _isOnline(url): #check if url is online
    pingresult = ping(url)
    if (not pingresult):
        # log.error(f"{url} està Offline")
        #todo vuere si la web esta offline desde la web
        return False
    else:
        # log.info(f"{url} is Online")
        return True

def getSecret(dir,usuari):    
    secrets = _cfgRead(f"{dir}/secrets")
    return secrets[usuari]

class Folder():    #first class test
    import os
    def __init__(self) -> None:
        pass

    def exists(self,directory):
        return self.os.path.exists(directory)

    def new(self,directory,verbose=False):
        if not self.exists(directory):
            try:
                self.os.makedirs(directory)
            except OSError:
                if verbose: print (f"Creation of the directory {directory} failed.")
                return False
            else:
                if verbose: print (f"Successfully created the directory {directory}")
                return True
        if verbose: print(f"folder {directory} already exist.")
        
    def extract(self,inputFile):
        splitInput=inputFile.split("/")
        if len(splitInput) > 1:
            extractedPath="/".join(splitInput[0:-1])
            self.new(extractedPath,verbose=True)

        else:
            print(f"{inputFile} is a file")


def getFileSize(file):
    return os.path.getsize(file)  
    
def fileExists(directory):
    return os.path.exists(directory)

def folderExists(directory):
    return os.path.exists(directory)

def folderCreate(directory):

    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError:
            print (f"Creation of the directory {directory} failed.")
            return False
        else:
            print (f"Successfully created the directory {directory}")
            return True
    print(f"folder {directory} already exist.")

def fivonacci(cycles=10,maxnum=0,lastvalue=False):
    # returns a fivonacci serie or the last value or the near value to spcecified maxnum value
    # print(fivonacci(5))
    # # [0, 1, 1, 2, 3]
    # print(fivonacci(5,lastvalue=4))
    # 3
    a, b = 0,1
    conta = 1
    cycles = cycles -2
    returnValue=[a,b]
    while True:
        if conta <= cycles:
            if maxnum == 0 or b < maxnum:
                a, b = b, a + b
                if maxnum == 0 or b < maxnum:
                    returnValue.append(b)
            conta+=1
        else:
            if lastvalue:
                return returnValue[-1]
            else:        
                return returnValue


def fivoWait(cycle,timefactor=1):
    from dtools import wait as _wait
    from dtools import fivonacci as fivo
    import random

    time=fivonacci(3+cycle,lastvalue=True)
    if timefactor==0:
        timefactor=random.uniform(0,1)
    _wait((time-1)*timefactor,(time)*timefactor)

def getCrc(file,buffersize = 65536):  # get crc value of a file
    try:
        with open(file, 'rb') as afile:
            buffr = afile.read(buffersize)
            crcvalue = 0
            while len(buffr) > 0:
                crcvalue = zlib.crc32(buffr, crcvalue)
                buffr = afile.read(buffersize)
    except:
        return False

    return (format(crcvalue & 0xFFFFFFFF, '08x'))

def _compareCrc(origin, compare):  # compares crc of 2 files
    originCrc = getCrc(origin)
    destinationCrc = getCrc(compare)
    print(originCrc)
    print(destinationCrc)
    if originCrc == destinationCrc:
        return True
    return False

def downloadDataImage(dataimage,filename="image",path="."):
    #based on https://stackoverflow.com/questions/30267199/downloading-image-data-uris-from-webpages-via-beautifulsoup
    # Separate the metadata from the image data
    head, data = dataimage.split(',', 1)
    # Get the file extension (gif, jpeg, png)
    file_ext = head.split(';')[0].split('/')[1]
    # Decode the image data
    plain_data = base64.b64decode(data)
    # Write the image to a file
    with open(f'{filename}.{file_ext}', 'wb') as f:
        f.write(plain_data)

def showError():
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print("Error: ",exc_type)
    print("File:",fname)
    print("Line:",exc_tb.tb_lineno)

def isString(val):    # return if a value is an string or not
    return isinstance(val,str)

def string2time(val):  # convert a string in seconds , example 1m = 60  
    if isString(val):
        multi = val[-1].lower()
        returnValue = int(val.lower().replace(multi,""))
        # print(f"returnvalue: {returnValue}")
        if multi == "m":
            returnValue = returnValue * 60
        elif multi == "h":
            returnValue = returnValue * 3600
        elif multi == "x":
            returnValue = returnValue * 0.001
    else:
        return val    

    return returnValue

def wait(start=1, end=0, comment=""):
    if end == 0:
        end = start
    timer = [string2time(start), string2time(end)]
    if timer[0] == timer[1]:
        timerResult = int(timer[0])
    else:
        timer = sorted(timer)
        timerResult = round(random.uniform(timer[0], timer[1]), 2)
    if comment != "":
        comment = f" {comment}"
    # log.debug(f'Wait{comment}, {timerResult} second{_getPlural(timerResult)}.')
    time.sleep(timerResult)


def save_cookie(driver, path):
    with open(path, 'w') as filehandler:
        json.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
    with open(path, 'r') as cookiesfile:
        cookies = json.load(cookiesfile)
    for cookie in cookies:
        driver.add_cookie(cookie)

def _setCookies(cookieFile):
    log.info(f"Loading {cookieFile}")    
    cookieValues = _loadFile(cookieFile)
    if cookieValues == False or os.path.getsize(cookieFile) == 0:
        log.warning("Do log in")
        wait(1,2)
        _acceptCookiePolicy()
        wait(1,2)
        _doLogIn(username,password)
        wait(1,2)
        _saveSessionInformation()
        wait(1,2)
        save_cookie(driver, cookieFile)
        # saveFile(cookieFile,driver.get_cookies(),True)
        # for cookie in driver.get_cookies():
        #     print(cookie)
    else :        
        log.warning("Setting saved cookie")
        load_cookie(driver, cookieFile)
        # for cookieValue in cookieValues:
        #     print(dict(cookieValue))
        #     # driver.add_cookie({'domain': '.instagram.com', 'expiry': 1602870612, 'httpOnly': True, 'name': 'shbid', 'path': '/', 'secure': True, 'value': '17599'})
        #     exit()
        wait(1,2)
        driver.get("https://"+url)
    
    wait(1,2)

   
# del _login(username,password):
def _saveSessionInformation():
    driver.implicitly_wait(2) # set load wait 1
    #-------------- # close popups
    try: # wait for page load
        WebDriverWait(driver, g_browserTimeOut).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.sqdOP.yWX7d.y3zKF')))
        try:
            wait(1,2)    
            driver.find_element_by_css_selector('.sqdOP.yWX7d.y3zKF').click()
            log.info("Save session info")
            return True
        except:
            log.warning("Save session info, Failure")
            return False
    except Exception as errorEx:
        _showError(errorEx)
        log.warning(f"Page waited {g_browserTimeOut} seconds.")
        return False



def ping(host,repeat=1):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host ]
    response = os.system(f'ping {host} {param} {repeat} > trash.txt')
    return response == 0
    #convertim un text en integre eliminant signes de puntuacio

