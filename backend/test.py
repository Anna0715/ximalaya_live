import ast
import json

t='[{"buyAlbums":{"canCombine":true,"canTransfer":true,"count":0,"detail":[],"type":"buy"},"canCombine":true,"canTransfer":true,"combineAbleThirdpartyBindInfo":{"canCombine":true,"canTransfer":true,"thirdpartyBindInfoList":[]},"coupons":[{"canCombine":true,"canTransfer":true,"count":0,"detail":[],"type":"coupon"},{"canCombine":true,"canTransfer":true,"count":0,"detail":[],"type":"voucher"}],"giftAlbums":{"canCombine":true,"canTransfer":true,"count":0,"detail":[],"type":"gift"},"knowledgeAmbassadorInfo":{"ambassador":false,"canCombine":true,"canTransfer":true},"liveInfo":{"canCombine":true,"canTransfer":true,"liveUser":false},"mainAccount":true,"mobile":"16621325482","nickname":"Anna1294839","pointInfo":{"canCombine":true,"canTransfer":true,"num":0},"points":0,"registerTime":"2022-12-12 13:46:01","subscribeAlbums":{"canCombine":true,"canTransfer":true,"count":0,"detail":[],"type":"subscription"},"thirdpartyBindInfos":[],"timeLimitAlbums":{"canCombine":true,"canTransfer":true,"count":0,"detail":[],"type":"timeLimit"},"tradeOrderInfo":{"canCombine":true,"canTransfer":true,"count":0,"detail":[]},"uid":1294839,"verifyInfo":{"canCombine":true,"canTransfer":true,"verify":true},"vips":[{"canCombine":true,"canTransfer":true,"detail":{"normalNip":false,"remainingVipDays":0,"unionVip":false,"vipScribe":false,"vipTrying":false},"type":"main"},{"canCombine":true,"canTransfer":true,"detail":{"normalNip":false,"remainingVipDays":0,"unionVip":false,"vipScribe":false,"vipTrying":false},"type":"kid"},{"canCombine":true,"canTransfer":true,"detail":{"normalNip":false,"remainingVipDays":0,"unionVip":false,"vipScribe":false,"vipTrying":false},"type":"dingKong"}],"virtualCurrencies":[{"androidAmount":1000.0,"canCombine":true,"canTransfer":true,"iosAmount":0.0,"type":"xidian"},{"androidAmount":98929.0,"canCombine":true,"canTransfer":true,"iosAmount":15409.0,"type":"xizuan"},{"androidAmount":0.0,"canCombine":true,"canTransfer":true,"iosAmount":0.0,"type":"guizuxizuan"},{"androidAmount":0.0,"canCombine":true,"canTransfer":true,"iosAmount":0.0,"type":"hongbao"},{"androidAmount":0.0,"canCombine":true,"canTransfer":true,"iosAmount":0.0,"type":"dushubi"}]}]'
lis=json.loads(t[1:-1])
print(lis,'\n',type(lis))

#测试一下
# 测试远程分支