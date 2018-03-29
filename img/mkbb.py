#!/usr/bin/env python
# coding:UTF-8

##################################################
# 必ずbbファイルを生成したいディレクトリにこのファイルを
# 置いて実行すること！
# (ebbにはファイルのフルパスを渡すことができない)
##################################################

import os
import subprocess

EBB_DIR = os.path.dirname(os.path.abspath(__file__))

for root, dirs, files in os.walk(EBB_DIR):
	for file in files:
		if file[-4:] == '.png':
			proc = subprocess.Popen(['ebb', file])
			proc.wait()
