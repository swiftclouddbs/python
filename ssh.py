import os
import sys
import subprocess

if os.path.exists("remote-output"):
	os.remove("remote-output")
else:
	print("No remote output here")


sys.stdout = open('remote-output', 'w')


print(os.popen("ssh -i ssh-key-2022-xx-13.key opc@129.213.xxx.xxx \"ls; pwd; date\"").read())



sys.stdout.close()
