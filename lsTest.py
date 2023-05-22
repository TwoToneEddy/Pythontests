
import sys
import os
from subprocess import Popen, PIPE
import argparse


stdout = Popen(f"grep -nr mks937z /home/lee/work/",shell=True,stdout=PIPE).stdout.read().decode()
print(len(stdout))
