#!/bin/bash
umask 022 # 保证后续流程文件权限正确
nohup /usr/bin/python3 /release/relayer.py -c /release/config/qtsource.rc > /tmp/std.out 2>&1

while true; do sleep 1; done

#project name
#project='ximalaya_live'
#currentdir="/release"
#var_dir="/release"
#run_log="${var_dir}/run-`hostname`.log"
#chmod 777 -R ${currentdir}
#if [ ! -d $var_dir  ];then
#        mkdir -p $var_dir
#        echo create $var_dir
#else
#        echo dir exist
#start() {
#        echo "starting"
#        cd ${currentdir}
#        exec ${currentdir}/run.sh >>$run_log 2>&1 &
#        echo "start completed"
#}
start