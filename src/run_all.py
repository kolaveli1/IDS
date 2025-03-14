import subprocess


scripts = [
    "detect_port_scan.py",
    "detect_mitm.py",
    "detect_ddos.py"
]


processes = []
for script in scripts:
    print(f"Starting {script}...")
    p = subprocess.Popen(["python3", f"src/{script}"])
    processes.append(p)


for p in processes:
    p.wait()
