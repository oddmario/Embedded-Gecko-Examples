import win32gui
import os
import subprocess
import pathlib
import time
import tempfile
import random
import string
import shutil
import atexit

temp_dir = ""

def exit_handler():
    if temp_dir != "":
        while True:
            try:
                shutil.rmtree(temp_dir, ignore_errors=False)
                break
            except Exception as e:
                pass
            time.sleep(1)

def CreateGeckoWindow_Windows(title, x, y, w, h, url):
    global temp_dir
    
    from platforms import windows as geWindows
    
    temp_dir = tempfile.mkdtemp()
    
    firefoxWindowIdentifier = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
    
    with open(os.path.join(temp_dir, "initFirefox.html"), "w") as f:
        f.write("""
        <html>
            <head>
                <title>""" + firefoxWindowIdentifier + """</title>
                <script>
                    window.location.replace('""" + url + """');
                </script>
            </head>
        </html>
        """)
        
    currentPath = pathlib.Path(__file__).parent.resolve()
    sampleProfilePath = os.path.join(currentPath, "firefox/profiles/profile.default-release")
    
    # Copy the sample profile to our temporary directory
    shutil.copytree(sampleProfilePath, os.path.join(temp_dir, "firefoxProfile"))
    
    firefoxExecutablePath = os.path.join(currentPath, "firefox/base/FirefoxPortable/App/Firefox64/firefox.exe")
    
    firefoxProcess = subprocess.Popen([firefoxExecutablePath, "-profile", os.path.join(temp_dir, "firefoxProfile"), "-url", "file:///" + os.path.join(temp_dir, "initFirefox.html").replace("\\", "/")])
    
    hwnd = 0
    while True:
        hwnd = win32gui.FindWindow(None, firefoxWindowIdentifier + " — Mozilla Firefox")
        if hwnd == 0:
            time.sleep(1)
        else:
            break
    
    geWindows.run_app(hwnd, title, x, y, w, h)
    
def CreateGeckoWindow_Linux():
    # TODO
    pass
    
def CreateGeckoWindow_OSX():
    # TODO
    pass
    
if __name__ == "__main__":
    atexit.register(exit_handler)
    
    if os.name == "posix":
        print("Your operating system isn't supported yet.")
        sys.exit()
        
    CreateGeckoWindow_Windows("GeckoEmbed - Test", 100, 100, 800, 600, "https://google.com")