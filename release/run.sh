#!/bin/bash

umask 022 # 保证后续流程文件权限正确
nohup /usr/bin/python3 /release/relayer.py -c /release/config/qtsource.rc > /tmp/std.out 2>&1

while true; do sleep 1; done