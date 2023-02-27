#!/bin/bash

main_dir="$(cd `ximalaya_live $0`; pwd)"

version=$1

pack_echo()
{
    echo "[pack.sh-info]: $1"
}

if [ $# != 1 ]
then
    pack_echo "./pack.sh [uat/production]"
    exit -1
fi

if [ "$version" != "uat" ] && [ "$version" != "production" ]; then
    pack_echo "unknown version, need \"uat\" or \"production\""
    exit -1
fi

pack_echo "start packaging..."

# 这里是你的构建脚本

pack_echo "packaging finished"

exit 0