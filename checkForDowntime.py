import requests
import os
r = str(requests.get("http://crm.menerga.no/mine_oppdrag.asp").content)
locateError = r.find('An error occurred on the server when processing the URL. Please contact the system administrator.')
if locateError!= -1:
    print('Restarting')
    os.system('start cmd /k iisreset')