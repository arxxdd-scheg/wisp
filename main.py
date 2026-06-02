import os
import time
import subprocess
import shutil
from colorama import Fore
def nameop():
    try:
        with open("lists/nnd.txt", "r") as f:
            return f.read()    
    except FileNotFoundError:
        print("nameop@err-; fnf.error")
        udun = input("namewr@write: ")
        with open("lists/nnd.txt", "w") as f:
            f.write(udun)
        return udun
def namewr(udun):
    with open("lists/nnd.txt", "w") as f:
        f.write(udun)
def cls():
    os.system('cls')
udun = nameop()
if udun:
    print("nameop@suc; udun.read/" + f"{udun}")
else:
    udun = input("namewr@write: ")
    namewr(udun)
time.sleep(0.3)
cls()
history = []
aliases = {}
try:
    with open("lists/aliases.txt", "r") as f:
        for line in f:
            if '=' in line:
                name, cmd = line.strip().split('=', 1)
                aliases[name] = cmd
except FileNotFoundError:
    pass
while True:
    bash = input(Fore.LIGHTGREEN_EX + f"{udun}@command" + Fore.WHITE + ": ")
    original_bash = bash
    parts = bash.split()
    if parts and parts[0].lower() in aliases:
        new_cmd = aliases[parts[0].lower()]
        if len(parts) > 1:
            bash = new_cmd + " " + " ".join(parts[1:])
        else:
            bash = new_cmd
    if bash.lower() == 'whoami':
        print(udun)
        history.append(original_bash)
    elif bash.lower() == 'time':
        print(time.strftime("bash; %H-%M-%S"))
        history.append(original_bash)
    elif bash.lower() == 'date':
        print(time.strftime("bash; %Y.%m.%d"))
        history.append(original_bash)
    elif bash.lower() == 'datetime':
        print(time.strftime("bash; %Y.%m.%d, %H-%M-%S"))
        history.append(original_bash)
    elif bash.lower().startswith('bash user -:; '):
        say = bash[14:]
        print(f"bash; {say}")
        history.append(original_bash)
    elif bash.lower() == 'stop -op':
        os.makedirs("lists", exist_ok=True)
        with open("lists/aliases.txt", "w") as f:
            for name, cmd in aliases.items():
                f.write(f"{name}={cmd}\n")
        break
    elif bash.lower() == 'disk':
        usage = shutil.disk_usage('/')
        print(f"bash; free: {usage.free // (2**30)}GB / total: {usage.total // (2**30)}GB")
    elif bash.lower() == 'clear -c':
        cls()
        history.append(original_bash)
    elif bash.lower() == 'clear -h':
        history = []
        print("bash; history is clear")
    elif bash.lower() == 'history':
        if history == []:
            print("bash; history is empty")
        else:
            for i, cmd in enumerate(history, 1):
                print(f"{i}. {cmd}")
        history.append(original_bash)
    elif bash.lower().startswith('alias '):
        parts = bash[6:].split('=', 1)
        if len(parts) == 2:
            alias_name = parts[0].strip()
            alias_command = parts[1].strip()
            aliases[alias_name] = alias_command
            print(f"bash; alias {alias_name} | {alias_command}")
            history.append(original_bash)
        else:
            print(Fore.RED + "bash-;" + Fore.WHITE + "use: alias name=command")
    elif bash.lower() == 'aliases':
        if aliases:
            for name, cmd in aliases.items():
                print(f"{name} | {cmd}")
        else:
            print("bash; aliases is empty")
        history.append(original_bash)
    elif bash.lower().startswith('unalias '):
        arg = bash[8:].strip()
        if arg == '-all':
            aliases.clear()
            os.makedirs("lists", exist_ok=True)
            with open("lists/aliases.txt", "w") as f:
                pass  
            print("bash; all aliases deleted")
            history.append(original_bash)
        else:
            alias_name = arg
            if alias_name in aliases:
                del aliases[alias_name]
                os.makedirs("lists", exist_ok=True)
                with open("lists/aliases.txt", "w") as f:
                    for name, cmd in aliases.items():
                        f.write(f"{name}={cmd}\n")
                print(f"bash; alias {alias_name} deleted")
                history.append(original_bash)
            else:
                print(Fore.RED + "bash-; " + Fore.WHITE + f"alias '{alias_name}' not found")
    elif bash.lower().startswith('run '):
        prog = bash[4:].strip()
        try:
            os.startfile(prog)
            print(f"bash; file {prog} started")
            history.append(original_bash)
        except Exception as e:
            try:
                os.system(f'start "" "{prog}"')
                print(f"bash; file {prog} started")
                history.append(original_bash)
            except Exception as e2:
                print(Fore.RED + "bash-; " + Fore.WHITE + f"file '{prog}' not found or cannot open")
    elif bash.lower() == 'start boot -g -os -up':
        print("boot; start with flags -g / -os / -up")
        time.sleep(3)
        print("boot; succes, found boot 'gui.pyw'. start...")
        time.sleep(1)
        subprocess.Popen("wisper.exe")
        os._exit(0)
    else:
        print(Fore.RED + "bash-; " + Fore.WHITE + f"command '{original_bash}' not found")