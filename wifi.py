import subprocess

result = subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=disable", shell=True, stdout=subprocess.PIPE])
print(result.stdout.decode("utf-8").strip())
