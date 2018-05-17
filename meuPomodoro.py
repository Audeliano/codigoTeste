import time
import webbrowser

loop = 0
total_breaks = 3

while(loop < total_breaks):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=HgzGwKwLmgM")
    loop = loop + 1
    
