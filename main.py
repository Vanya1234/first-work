import platform, os, socket, sys, json, locale
from datetime import datetime
import psutil


name_os = platform.system()
arc = platform.machine()
username = os.environ.get("USERNAME") or os.environ.get("USER")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
proc = platform.processor()
info = platform.uname()
cores = os.cpu_count()
time = datetime.now()
language = locale.getlocale()
memory = psutil.virtual_memory().total/(2**20)
memory_used = psutil.virtual_memory().used/(2**20)
memory_free = psutil.virtual_memory().free/(2**20)

processes = []

for process in psutil.process_iter(
    attrs = ['pid', 'name', 'status', 'create_time', 'memory_info', 'cpu_percent'],
    ad_value=None
):  
    if len(processes) == 10:
        break
    f = 0
    memory_bytes = process.info['memory_info']
    if memory_bytes is None:
        f = 1
    cpu = process.info['cpu_percent']
    if cpu is None:
        f = 1
    if f == 0 and process.info['status'] == 'running':
        process.info['memory_info'] = memory_bytes.rss/(2**20)
        processes.append(process.info)

print(processes)
print(memory)
print(memory_used)
print(memory_free)
print(info.node)
print(info.release)
print(info.version)
print(username)
print(ip)
print(name_os)
print(arc)
print(proc)
print(cores)
print(sys.version)
print(sys.executable)
print(time)
print(language)
