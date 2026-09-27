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

processes_all = []

for process in psutil.process_iter(
    attrs = ['pid', 'name', 'status', 'create_time', 'memory_info'],
    ad_value=None
):  
    info_prog = process.info
    pid = info_prog['pid']
    name = info_prog['name']
    status = info_prog['status']
    create_time = info_prog['create_time']
    memory_info = info_prog['memory_info']
    time_prog = datetime.fromtimestamp(create_time)
    if (memory_info is not None) and (status == psutil.STATUS_RUNNING):
        memory_info = memory_info.rss/(2**20)
        prog = {
            'pid': pid,
            'name': name,
            'status': status,
            'memory_info': memory_info,
            'create_time': time_prog.strftime("%d.%m.%Y %H:%M:%S"),
        }
        processes_all.append(prog)

processes_all.sort(key=lambda proc: proc["memory_info"], reverse=True)


info_and_proc = {
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
    'process_1': processes_all[0],
    'process_2': processes_all[1],
    'process_3': processes_all[2],
    'process_4': processes_all[3],
    'process_5': processes_all[4],
    'process_6': processes_all[5],
    'process_7': processes_all[6],
    'process_8': processes_all[7],
    'process_9': processes_all[8],
    'process_10': processes_all[9],
}


with open("system_info.json", "w", encoding="utf-8") as file:
    json.dump(info_and_proc, file, ensure_ascii= False, indent = 2)