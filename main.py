import json
import os
import subprocess

localCmd = "git branch --list"
remoteCmd = "git ls-remote --heads origin"
RELEASESUB = "release/"
MASTERSUB = "master"

s = subprocess.Popen([localCmd], shell=True, stdout=subprocess.PIPE).stdout
service_state = s.read().splitlines()

res = subprocess.Popen([remoteCmd], shell=True, stdout=subprocess.PIPE).stdout
gitRes = res.read().splitlines()
print("Fount Remote")

for key in list(service_state):
    if MASTERSUB in key:
        service_state.remove(key)
        continue
    if RELEASESUB in key:
        service_state.remove(key)
        continue
    if any(li in key for li in gitRes):
        service_state.remove(key)

for remain in list(service_state):
    print(remain)
    inp = raw_input("Remove y/n ")
    if inp == "n":
        service_state.remove(remain)

for remain in list(service_state):
    print(remain)
 
finalInp = raw_input("Do you want to remove y/n ")
if finalInp == "y":
    for remain in service_state:
        res = subprocess.Popen(["git branch -D %s" % (remain)], shell=True, stdout=subprocess.PIPE).stdout
