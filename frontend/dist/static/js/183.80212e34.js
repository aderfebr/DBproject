"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[183],{183:function(l,t,n){n.r(t),n.d(t,{default:function(){return z}});var d=n(3396),e=n(7139);const i=l=>((0,d.dD)("data-v-e819a022"),l=l(),(0,d.Cn)(),l),u={id:"main"},a={key:0,id:"popAdd"},_=i((()=>(0,d._)("div",{id:"header"}," 添加数据",-1))),o=i((()=>(0,d._)("div",{id:"body"},null,-1))),s={id:"footer"},r={id:"left"},h=i((()=>(0,d._)("i",{class:"fa fa-home"},null,-1))),c={id:"selected"},f=i((()=>(0,d._)("i",{class:"fa fa-street-view"},null,-1))),w={id:"right"},v={id:"top"},k=i((()=>(0,d._)("li",null,[(0,d._)("h1",null,[(0,d.Uk)(" "),(0,d._)("i",{class:"fa fa-street-view"}),(0,d.Uk)(" 人员")])],-1))),b=i((()=>(0,d._)("div",{style:{clear:"both"}},null,-1))),p={id:"container"},g=i((()=>(0,d._)("br",null,null,-1))),m=i((()=>(0,d._)("thead",null,[(0,d._)("tr",null,[(0,d._)("th",null,"员工编号"),(0,d._)("th",null,"加入时间"),(0,d._)("th",null,"姓名"),(0,d._)("th",null,"用户名"),(0,d._)("th",null,"操作")])],-1))),y=i((()=>(0,d._)("td",null,[(0,d._)("button",{id:"change"},"更改"),(0,d.Uk)(" "),(0,d._)("button",{id:"delete"},"删除")],-1)));function A(l,t,n,i,A,C){const D=(0,d.up)("router-link");return(0,d.wg)(),(0,d.iD)("div",u,[A.showAdd?((0,d.wg)(),(0,d.iD)("div",a,[_,o,(0,d._)("div",s,[(0,d._)("button",{onClick:t[0]||(t[0]=l=>A.showAdd=0)},"   确认   ")])])):(0,d.kq)("",!0),(0,d._)("div",r,[(0,d._)("ul",null,[(0,d._)("li",null,[(0,d.Wm)(D,{to:"/"},{default:(0,d.w5)((()=>[h,(0,d.Uk)(" 首页")])),_:1})]),(0,d._)("li",c,[(0,d.Wm)(D,{to:"/"},{default:(0,d.w5)((()=>[f,(0,d.Uk)(" 人员")])),_:1})])])]),(0,d._)("div",w,[(0,d._)("div",v,[(0,d._)("ul",null,[k,(0,d._)("li",null,[(0,d._)("button",{id:"add",onClick:t[1]||(t[1]=l=>A.showAdd=1)},"添加")])]),b]),(0,d._)("div",p,[g,(0,d._)("table",null,[m,(0,d._)("tbody",null,[((0,d.wg)(!0),(0,d.iD)(d.HY,null,(0,d.Ko)(A.content,(l=>((0,d.wg)(),(0,d.iD)("tr",null,[(0,d._)("td",null,(0,e.zw)(l.staff_id),1),(0,d._)("td",null,(0,e.zw)(l.join_id),1),(0,d._)("td",null,(0,e.zw)(l.name),1),(0,d._)("td",null,(0,e.zw)(l.username),1),y])))),256))])])])])])}var C={data(){return{content:null,showAdd:0}},created(){this.getdata()},methods:{getdata(){this.axios.get("http://localhost:8000/api/query/").then((l=>{this.content=l.data}))}}},D=n(89);const U=(0,D.Z)(C,[["render",A],["__scopeId","data-v-e819a022"]]);var z=U}}]);
//# sourceMappingURL=183.80212e34.js.map