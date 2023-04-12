"use strict";(self["webpackChunkvue_antd_pro"]=self["webpackChunkvue_antd_pro"]||[]).push([[52],{52:function(e,t,a){a.r(t),a.d(t,{default:function(){return f}});a(74916),a(15306);var o=function(){var e=this,t=e._self._c;return t("div",[t("a-form",{attrs:{"label-col":{span:3},"wrapper-col":{span:16},form:e.form},on:{submit:e.onSubmit}},[t("a-form-item",{attrs:{label:e.$t("createCourseLive.uid")}},[t("a-input",{directives:[{name:"decorator",rawName:"v-decorator",value:["uids",{rules:[{required:!0,message:"请输入uid"}]}],expression:"[\n          `uids`,\n          {\n            rules: [\n              {\n                required: true,\n                message: '请输入uid',\n              },\n            ],\n          },\n        ]"}],attrs:{type:"text",placeholder:e.$t("createCourseLive.uid.placeholder")}})],1),t("a-form-item",{attrs:{label:e.$t("createCourseLive.dropdown.label")}},[t("a-select",{ref:"select",staticStyle:{width:"120px"},on:{change:e.handleDropdownChange},model:{value:e.dropdownValue,callback:function(t){e.dropdownValue=t},expression:"dropdownValue"}},[t("a-select-option",{attrs:{value:"pay"}},[e._v(e._s(e.$t("createCourseLive.dropdown.pay.type")))]),t("a-select-option",{attrs:{value:"formal"}},[e._v(e._s(e.$t("createCourseLive.dropdown.formal.type")))]),t("a-select-option",{attrs:{value:"test"}},[e._v(e._s(e.$t("createCourseLive.dropdown.test.type")))])],1)],1),t("a-form-item",{attrs:{label:e.$t("createCourseLive.range.time")}},[t("a-range-picker",{attrs:{format:"YYYY-MM-DD HH:mm:ss"},on:{change:e.rangeTimeChange},model:{value:e.rangeTime,callback:function(t){e.rangeTime=t},expression:"rangeTime"}})],1),t("a-row",[t("a-col",{attrs:{span:1}}),t("a-col",{attrs:{span:6}},[t("a-form-item",{attrs:{label:e.$t("createCourseLive.ticket.price"),"label-col":{span:8}}},[t("a-input-number",{attrs:{min:0,formatter:function(e){return"$ ".concat(e).replace(/\B(?=(\d{3})+(?!\d))/g,",")},parser:function(e){return e.replace(/\$\s?|(,*)/g,"")}},model:{value:e.price,callback:function(t){e.price=t},expression:"price"}})],1)],1),t("a-col",{attrs:{span:6}},[t("a-form-item",{attrs:{label:e.$t("createCourseLive.stock"),"label-col":{span:8}}},[t("a-input-number",{attrs:{min:0},model:{value:e.stock,callback:function(t){e.stock=t},expression:"stock"}})],1)],1),t("a-col",{attrs:{span:6}},[t("a-form-item",{attrs:{label:e.$t("createCourseLive.ticket.sharing"),"label-col":{span:8}}},[t("a-input-number",{attrs:{min:0,max:70,formatter:function(e){return"".concat(e,"%")},parser:function(e){return e.replace("%","")}},model:{value:e.ticketSharing,callback:function(t){e.ticketSharing=t},expression:"ticketSharing"}})],1)],1)],1),t("a-row",[t("a-col",{attrs:{span:1}}),t("a-col",{attrs:{span:6}},[t("a-form-item",{attrs:{label:e.$t("createCourseLive.open.sale.check"),"label-col":{span:8}}},[t("a-switch",{attrs:{checked:e.openSale},on:{change:e.onOpenSaleChange}})],1)],1),t("a-col",{attrs:{span:6}},[t("a-form-item",{attrs:{label:e.$t("createCourseLive.open.play.back"),"label-col":{span:8}}},[t("a-tooltip",{scopedSlots:e._u([{key:"title",fn:function(){return[e._v(e._s(e.$t("createCourseLive.open.play.back.tip")))]},proxy:!0}])},[t("a-switch",{attrs:{checked:e.showPlayback,disabled:!0}})],1)],1)],1),t("a-col",{attrs:{span:6}},[t("a-form-item",{attrs:{label:e.$t("createCourseLive.open.send.gift"),"label-col":{span:8}}},[t("a-switch",{attrs:{checked:e.openSendGift},on:{change:e.onOpenSendGiftChange}})],1)],1)],1),t("a-form-item",{attrs:{"wrapper-col":{span:14,offset:4}}},[t("a-button",{attrs:{type:"primary","html-type":"submit"}},[e._v("操作")]),t("a-button",{staticStyle:{"margin-left":"10px"},on:{click:e.resetForm}},[e._v("重置")])],1)],1),t("a-table",{attrs:{dataSource:e.dataSource,columns:e.columns,bordered:"",loading:e.tableLoading},scopedSlots:e._u([{key:"title",fn:function(){return[e._v(e._s(e.tableTitle))]},proxy:!0}])})],1)},n=[],r=(a(7672),a(61446)),i=(a(41539),a(39714),a(21249),a(92222),a(84963)),l=a(30381),s=a.n(l),c="YYYY-MM-DD HH:mm:ss",u={name:"CreateCourseLive",data:function(){return{form:this.$form.createForm(this,{name:"CreateCourseLive"}),uids:"",dropdownValue:"pay",rangeTime:[s()().add(20,"m").format(c),s()().add(50,"m").format(c)],price:10,stock:1e3,ticketSharing:50,openSale:!0,openSendGift:!0,showPlayback:!0,dataSource:[],tableTitle:"请求uid数量：0，成功数量：0",tableLoading:!1,columns:[{title:"uid",dataIndex:"uid",key:"uid",align:"center"},{title:"返回信息",dataIndex:"response",key:"response",align:"center"}]}},methods:{handleDropdownChange:function(e){this.dropdownValue=e,this.showPlayback="test"!==e},rangeTimeChange:function(e){var t,a;this.rangeTime=[null===e||void 0===e||null===(t=e[0])||void 0===t?void 0:t.format(c),null===e||void 0===e||null===(a=e[1])||void 0===a?void 0:a.format(c)]},onOpenSaleChange:function(){this.openSale=!this.openSale},onOpenSendGiftChange:function(){this.openSendGift=!this.openSendGift},resetForm:function(){this.form.resetFields(),this.dropdownValue="pay",this.rangeTime=[s()().add(20,"m").format(c),s()().add(50,"m").format(c)],this.price=10,this.stock=1e3,this.ticketSharing=50,this.openSale=!0,this.openSendGift=!0,this.showPlayback=!0},onSubmit:function(e){e.preventDefault();var t=this;this.form.validateFields((function(e,a){var o,n,l,s,c;e||(t.uids=null===a||void 0===a?void 0:a.uids,t.uids&&(t.dataSource=[],t.tableLoading=!0,(0,i.EG)({uid:t.uids,coursetype:t.dropdownValueBeCourseType(t.dropdownValue),openGoods:null===(o=t.openSale)||void 0===o?void 0:o.toString(),openGift:null===(n=t.openSendGift)||void 0===n?void 0:n.toString(),showPlayback:null===(l=t.showPlayback)||void 0===l?void 0:l.toString(),startAt:null===(s=t.rangeTime)||void 0===s?void 0:s[0],endAt:null===(c=t.rangeTime)||void 0===c?void 0:c[1],price:t.price,quantity:t.stock,clearRate:t.ticketSharing}).then((function(e){if(200===e.code&&null!==e&&void 0!==e&&e.data){var a,o=0;null===e||void 0===e||null===(a=e.data)||void 0===a||a.map((function(e,a){t.dataSource.push({key:a+1+"",uid:null===e||void 0===e?void 0:e.uid,response:null===e||void 0===e?void 0:e.msg}),"success"===(null===e||void 0===e?void 0:e.CeatecourseLive)&&(o+=1)})),t.tableTitle="请求uid数量：".concat(t.dataSource.length,"，成功数量：").concat(o)}else r.Z.error((null===e||void 0===e?void 0:e.msg)||"出错了，请@张柔"),t.tableTitle=(null===e||void 0===e?void 0:e.msg)||"出错了，请@张柔";t.tableLoading=!1})).catch((function(e){r.Z.error((null===e||void 0===e?void 0:e.msg)||"出错了，请@张柔"),t.tableTitle=(null===e||void 0===e?void 0:e.msg)||"出错了，请@张柔",t.tableLoading=!1}))))}))},dropdownValueBeCourseType:function(e){switch(e){case"pay":return"付费";case"formal":return"正式";case"test":return"测试";default:return"付费"}}}},d=u,p=a(1001),m=(0,p.Z)(d,o,n,!1,null,"01f91d78",null),f=m.exports},84963:function(e,t,a){a.d(t,{EG:function(){return l},s0:function(){return i}});var o=a(76166),n="http://ops.test.ximalaya.com/ximalive-qa",r={addVprofileVerify:"/AddVprofileVerify",createCourseLive:"/CreateCourseLive"};function i(e){return(0,o.ZP)({url:n+r.addVprofileVerify,method:"POST",data:JSON.stringify(e),headers:{"Content-Type":"application/json;charset=UTF-8"}})}function l(e){return(0,o.ZP)({url:n+r.createCourseLive,method:"POST",data:JSON.stringify(e),headers:{"Content-Type":"application/json;charset=UTF-8"}})}}}]);