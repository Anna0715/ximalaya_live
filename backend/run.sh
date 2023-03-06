#!/bin/sh

export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
export OMP_NUM_THREADS=1

#project name
project='ximalaya_live'
currentdir="/usr/local/tfs-publish/${project}"
var_dir="/var/log/tfs-publish/${project}"
run_log="${var_dir}/run-`hostname`.log"
umask 022
python main.py > /tmp/out.log

chmod 777 -R ${currentdir}

if [ ! -d $var_dir  ];then
        mkdir -p $var_dir
        echo create $var_dir
else
        echo dir exist
fi

start() {
        echo "starting"
        cd ${currentdir}
        exec ${currentdir}/model_run.sh >>$run_log 2>&1 &
        echo "start completed"
}
start
