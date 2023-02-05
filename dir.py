import subprocess

result = subprocess.run("dir", shell=True, stdout=subprocess.PIPE)
print(result.stdout.decode("utf-8").strip())
