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
    attrs = ['pid', 'name', 'status', 'create_time', 'memory_info'],
    ad_value=None
):  
    info_prog = process.info
    pid = info_prog['pid']
    name = info_prog['name']
    status = info_prog['status']
    create_time = info_prog['create_time']
    try:
        cpu_per = process.cpu_percent(interval=1)

    except (
        psutil.AccessDenied,
        psutil.NoSuchProcess,
        psutil.ZombieProcess
    ):
        continue
    memory_info = info_prog['memory_info']
    if (memory_info is not None) and (status == psutil.STATUS_RUNNING) and (cpu_per > 0):
        memory_info = memory_info.rss/(2**20)
        prog = {
            'pid': pid,
            'name': name,
            'status': status,
            'cpu_percent': cpu_per,
            'memory_info': memory_info,
            'create_time': create_time,
        }
        processes.append(prog)

processes.sort(key=lambda proc: (proc["memory_info"], proc["cpu_percent"]), reverse=True)

information = {
    'OC': name_os,
    'version_OS': info.release,
    'Name_computer': info.node,
    'Username': username,
    'CPU_architecture': proc,
    'count_cores': cores,
    'RAM': memory,
    'RAM_used': memory_used,
    'RAM_free': memory_free,
    'ip_pc': ip,
    'Time': time.strftime("%d.%m.%Y %H:%M:%S"),
    'Python_path': sys.executable,
}

print(information)
print(processes)
