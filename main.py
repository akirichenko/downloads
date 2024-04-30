#!/opt/anaconda/bin/python3

import subprocess
import glob, os
import time
import curses

os.environ['TERM'] = 'xterm-256color'


def load_scripts(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]


def check_file(script):
    return os.path.isfile(f"{script}_done.txt")


def main(stdscr):
    # clean the status files
    for f in glob.glob("*_done.txt"):
        os.remove(f)

    # Clear screen
    stdscr.clear()

    scripts = load_scripts("scripts.txt")
    processes = {script: {"process": None, "status": "Not Ready"} for script in scripts}

    for script in scripts:
        processes[script]["process"] = subprocess.Popen(["python3", f"{script}.py"])

    some_crashed = False
    while True:
        all_done = True
        for i, (script, data) in enumerate(processes.items()):
            if data["process"].poll() is not None:
                if data["status"] == "Not Ready":
                    data["status"] = "Ready" if check_file(script) else "Crashed"
                    if data["status"] == "Crashed":
                        some_crashed = True
            stdscr.move(i, 0)
            stdscr.clrtoeol()
            stdscr.addstr(i, 0, f"{script}: {data['status']}")
            if data["status"] == "Not Ready":
                all_done = False
        if all_done:
            break
        stdscr.refresh()
        time.sleep(5)

    # Leave the content on the screen after exit
    if some_crashed:
        stdscr.addstr(5, 0, "\nSome scripts have failed...")
    else:
        stdscr.addstr(5, 0, "\nAll scripts have started...")
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
