import os
import subprocess

#subprocess.call('git init',shell = True)
#print('init done..')

subprocess.call('git add .',shell=True)
print('adding dne')
subprocess.call('git commit -m "committed"',shell=True)
subprocess.call('git remote add origin https://github.com/yasharvindsingh/oasystry.git',shell=True)
subprocess.call('git push',shell=True)
