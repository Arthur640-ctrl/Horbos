import threading
import asyncio
from start import check_start  
from app import app
import maintenance
from ws import ws
from report import report
from error import newError
from backup import backupProcess
from log import log

threadWS = threading.Thread(target=ws)

threadReport = threading.Thread(target=report)

threadBackups = threading.Thread(target=backupProcess)

log("info", "Launching server...")
try:
    check_start()
    log("info", "The launching thread successfully runs")
except Exception as e:
    newError("Critical", f"The server could not launch properly. Error: {e}")
    log("error", f"The server could not launch properly. Error: {e}")

try:
    threadWS.start()
    log("info", "The WebSocket thread successfully runs")
except Exception as e:
    newError("Critical", f"The WebSockets system could not start when launching the thread. Error : {e}")
    log("error", f"The WebSockets system could not start when launching the thread. Error : {e}")

try:
    threadReport.start()
    log("info", "The Report thread successfully runs")
except Exception as e:
    newError("Critical", f"The report system could not start when launching the thread. Error : {e}")
    log("error", f"The report system could not start when launching the thread. Error : {e}")

try:
    threadBackups.start()
    log("info", "The BackUp thread successfully runs")
except Exception as e:
    newError("Error", f"The backups system could not start when launching the thread. Error : {e}")
    log("error", f"The backups system could not start when launching the thread. Error : {e}")

try:
    asyncio.run(app())  
    log("info", "The App thread successfully runs")
except Exception as e:
    newError("Critical", f"The bot system could not start properly. Error: {e}")
    log("error", f"The bot system could not start properly. Error: {e}")
