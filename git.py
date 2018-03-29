import os
import subprocess
import sys

init_dir = sys.argv[2]+'/.git'
startup_repo = sys.argv[3]

if not os.path.isdir(init_dir):
    subprocess.call('git init',shell = True)
    subprocess.call('git add .',shell=True)
    subprocess.call('git commit -m "committed"',shell=True)
    subprocess.call('git remote add origin https://github.com/OASYS-SIH-2018/'+str(startup_repo),shell=True)
    subprocess.call('git push --set-upstream origin master',shell=True)
else:
    subprocess.call('git remote add origin https://github.com/OASYS-SIH-2018/'+str(startup_repo),shell=True)
    subprocess.call('git push --set-upstream origin master',shell=True)
