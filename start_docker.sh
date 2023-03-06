#!/bin/sh
# cd /home/virgpu/test_dx/content_pred

build_path=`pwd`
cd ${build_path}
rm -rf content_pred
git clone http://gitlab.ximalaya.com/rou.zhang/ximalaya_live.git
chmod -R 777 content_pred
docker build -t harbor102.test.ximalaya.com/test/ximalaya_live:$1 .
docker push harbor102.test.ximalaya.com/test/ximalaya_live:$1
