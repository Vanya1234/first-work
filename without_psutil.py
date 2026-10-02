import platform, os, socket, sys, json
from datetime import datetime

name_os = platform.system()
arc = platform.machine()
username = os.environ.get("USERNAME") or os.environ.get("USER")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
proc = platform.processor()
info = platform.uname()
cores = os.cpu_count()
time = datetime.now()

info_and_proc = {
    'OC': name_os,
    'version_OS': info.release,
    'Name_computer': info.node,
    'Username': username,
    'CPU_architecture': proc,
    'count_cores': cores,
    'ip_pc': ip,
    'Time': time.strftime("%d.%m.%Y %H:%M:%S"),
    'Python_path': sys.executable,
}


with open("system_info.json", "w", encoding="utf-8") as file:
    json.dump(info_and_proc, file, ensure_ascii= False, indent = 2)
