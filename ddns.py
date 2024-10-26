import requests
import time
import datetime
ip = ""
sip = ""
while 1:
  try:
    ip = (requests.get('https://api.ipify.org/', timeout = 5).text)
  except:
    ip = sip
  timex = datetime.datetime.now()
  timef = timex.strftime("%m/%d/%Y, %H:%M:%S")
  if(sip != ip):
    sip = ip
    tryb = True
    tmpw = "N/A"
    try:
      tmpw = (requests.get('https://freedns.afraid.org/dynamic/update.php?...', timeout = 3).text).strip()
    except:
      tryb = False
      sip = ""
    if(tryb):
      try:
        f1 = open("/root/ip-log.txt", "x")
      except:
        f1 = open("/root/ip-log.txt", "a")
      else:
        f1.write("asinbion github nanopineo-openvpn project\n")
      f1.write(timef + " | " + ip + " | " + tmpw + "\n")
      f1.close()
  time.sleep(5)
