"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[776],{9776:function(t,l,i){i.r(l),i.d(l,{default:function(){return X}});var e=i(3396),d=i(9242),o=i(7139);const n=t=>((0,e.dD)("data-v-e864be82"),t=t(),(0,e.Cn)(),t),a={id:"main"},_={key:0,id:"popAdd"},r=n((()=>(0,e._)("div",{id:"header"}," 添加数据",-1))),s={id:"body"},u={style:{flex:"1"}},h=n((()=>(0,e._)("br",null,null,-1))),p=n((()=>(0,e._)("br",null,null,-1))),c={style:{flex:"1"}},m=n((()=>(0,e._)("br",null,null,-1))),f={id:"footer"},w={key:1,id:"popAdd"},v=n((()=>(0,e._)("div",{id:"header"}," 更改数据",-1))),k={id:"body"},b={style:{flex:"1"}},y=n((()=>(0,e._)("br",null,null,-1))),g=n((()=>(0,e._)("br",null,null,-1))),U=n((()=>(0,e._)("br",null,null,-1))),C={style:{flex:"1"}},x=n((()=>(0,e._)("br",null,null,-1))),D=n((()=>(0,e._)("br",null,null,-1))),z={id:"footer"},V={id:"left"},A=n((()=>(0,e._)("i",{class:"fa fa-home"},null,-1))),W=n((()=>(0,e._)("i",{class:"fa fa-street-view"},null,-1))),T=n((()=>(0,e._)("i",{class:"fa fa-map-marker"},null,-1))),q=n((()=>(0,e._)("i",{class:"fa fa-wrench"},null,-1))),H=n((()=>(0,e._)("i",{class:"fa fa-shield"},null,-1))),K={id:"selected"},Y=n((()=>(0,e._)("i",{class:"fa fa-archive"},null,-1))),$=n((()=>(0,e._)("i",{class:"fa fa-bell"},null,-1))),M={id:"right"},j=n((()=>(0,e._)("div",{id:"top"},[(0,e._)("ul",null,[(0,e._)("li",null,[(0,e._)("h1",null,[(0,e.Uk)(" "),(0,e._)("i",{class:"fa fa-archive"}),(0,e.Uk)(" 运维系统")])])]),(0,e._)("div",{style:{clear:"both"}})],-1))),I={key:0,id:"container"},Z=n((()=>(0,e._)("br",null,null,-1))),B=n((()=>(0,e._)("thead",null,[(0,e._)("tr",null,[(0,e._)("th",null,"员工编号"),(0,e._)("th",null,"加入时间"),(0,e._)("th",null,"姓名"),(0,e._)("th",null,"操作")])],-1))),E=["onClick"],F={key:1,id:"container"},G=n((()=>(0,e._)("i",{class:"fa fa-arrow-circle-left"},null,-1))),J=n((()=>(0,e._)("br",null,null,-1))),L=n((()=>(0,e._)("thead",null,[(0,e._)("tr",null,[(0,e._)("th",null,"维护单编号"),(0,e._)("th",null,"维护时间"),(0,e._)("th",null,"维护描述"),(0,e._)("th",null,"设备编号"),(0,e._)("th",null,"员工编号"),(0,e._)("th",null,"操作")])],-1))),N=["onClick"],O=["onClick"];function P(t,l,i,n,P,Q){const R=(0,e.up)("router-link");return(0,e.wg)(),(0,e.iD)("div",a,[P.showAdd?((0,e.wg)(),(0,e.iD)("div",_,[r,(0,e._)("div",s,[(0,e._)("div",u,[(0,e._)("div",null,[(0,e.Uk)("维护时间"),h,(0,e.wy)((0,e._)("input",{type:"text","onUpdate:modelValue":l[0]||(l[0]=t=>P.mreport_date=t)},null,512),[[d.nr,P.mreport_date]])]),(0,e._)("div",null,[(0,e.Uk)("设备编号"),p,(0,e.wy)((0,e._)("select",{"onUpdate:modelValue":l[1]||(l[1]=t=>P.device_id_id=t)},[((0,e.wg)(!0),(0,e.iD)(e.HY,null,(0,e.Ko)(P.device,(t=>((0,e.wg)(),(0,e.iD)("option",null,(0,o.zw)(t),1)))),256))],512),[[d.bM,P.device_id_id]])])]),(0,e._)("div",c,[(0,e._)("div",null,[(0,e.Uk)("维护描述"),m,(0,e.wy)((0,e._)("input",{type:"text","onUpdate:modelValue":l[2]||(l[2]=t=>P.mreport=t)},null,512),[[d.nr,P.mreport]])])])]),(0,e._)("div",f,[(0,e._)("button",{style:{"background-color":"#28a745"},onClick:l[3]||(l[3]=t=>Q.add_commit())},"   确认   "),(0,e._)("button",{style:{"background-color":"#dc3545"},onClick:l[4]||(l[4]=t=>Q.cancel())},"   取消   ")])])):(0,e.kq)("",!0),P.showChange?((0,e.wg)(),(0,e.iD)("div",w,[v,(0,e._)("div",k,[(0,e._)("div",b,[(0,e._)("div",null,[(0,e.Uk)("维护单编号"),y,(0,e.wy)((0,e._)("input",{type:"text","onUpdate:modelValue":l[5]||(l[5]=t=>P.mreport_id=t),readonly:"readonly"},null,512),[[d.nr,P.mreport_id]])]),(0,e._)("div",null,[(0,e.Uk)("维护描述"),g,(0,e.wy)((0,e._)("input",{type:"text","onUpdate:modelValue":l[6]||(l[6]=t=>P.mreport=t)},null,512),[[d.nr,P.mreport]])]),(0,e._)("div",null,[(0,e.Uk)("员工编号"),U,(0,e.wy)((0,e._)("select",{"onUpdate:modelValue":l[7]||(l[7]=t=>P.staff_id_id=t)},[((0,e.wg)(!0),(0,e.iD)(e.HY,null,(0,e.Ko)(P.staff,(t=>((0,e.wg)(),(0,e.iD)("option",null,(0,o.zw)(t),1)))),256))],512),[[d.bM,P.staff_id_id]])])]),(0,e._)("div",C,[(0,e._)("div",null,[(0,e.Uk)("维护时间"),x,(0,e.wy)((0,e._)("input",{type:"text","onUpdate:modelValue":l[8]||(l[8]=t=>P.mreport_date=t)},null,512),[[d.nr,P.mreport_date]])]),(0,e._)("div",null,[(0,e.Uk)("设备编号"),D,(0,e.wy)((0,e._)("select",{"onUpdate:modelValue":l[9]||(l[9]=t=>P.device_id_id=t)},[((0,e.wg)(!0),(0,e.iD)(e.HY,null,(0,e.Ko)(P.device,(t=>((0,e.wg)(),(0,e.iD)("option",null,(0,o.zw)(t),1)))),256))],512),[[d.bM,P.device_id_id]])])])]),(0,e._)("div",z,[(0,e._)("button",{style:{"background-color":"#28a745"},onClick:l[10]||(l[10]=t=>Q.change_commit())},"   确认   "),(0,e._)("button",{style:{"background-color":"#dc3545"},onClick:l[11]||(l[11]=t=>Q.cancel())},"   取消   ")])])):(0,e.kq)("",!0),(0,e._)("div",V,[(0,e._)("ul",null,[(0,e._)("li",null,[(0,e.Wm)(R,{to:"/"},{default:(0,e.w5)((()=>[A,(0,e.Uk)(" 首页")])),_:1})]),(0,e._)("li",null,[(0,e.Wm)(R,{to:"/staff"},{default:(0,e.w5)((()=>[W,(0,e.Uk)(" 人员")])),_:1})]),(0,e._)("li",null,[(0,e.Wm)(R,{to:"/area"},{default:(0,e.w5)((()=>[T,(0,e.Uk)(" 区域")])),_:1})]),(0,e._)("li",null,[(0,e.Wm)(R,{to:"/device"},{default:(0,e.w5)((()=>[q,(0,e.Uk)(" 设备")])),_:1})]),(0,e._)("li",null,[(0,e.Wm)(R,{to:"/security"},{default:(0,e.w5)((()=>[H,(0,e.Uk)(" 安保系统")])),_:1})]),(0,e._)("li",K,[(0,e.Wm)(R,{to:"/maintain"},{default:(0,e.w5)((()=>[Y,(0,e.Uk)(" 运维系统")])),_:1})]),(0,e._)("li",null,[(0,e.Wm)(R,{to:"/alarm"},{default:(0,e.w5)((()=>[$,(0,e.Uk)(" 警报处理")])),_:1})])])]),(0,e._)("div",M,[j,P.info?(0,e.kq)("",!0):((0,e.wg)(),(0,e.iD)("div",I,[Z,(0,e._)("table",null,[B,(0,e._)("tbody",null,[((0,e.wg)(!0),(0,e.iD)(e.HY,null,(0,e.Ko)(P.content,(t=>((0,e.wg)(),(0,e.iD)("tr",null,[(0,e._)("td",null,(0,o.zw)(t.staff_id),1),(0,e._)("td",null,(0,o.zw)(t.join_id),1),(0,e._)("td",null,(0,o.zw)(t.name),1),(0,e._)("td",null,[(0,e._)("button",{id:"info",onClick:l=>Q.open(t.staff_id)},"详情",8,E)])])))),256))])])])),P.info?((0,e.wg)(),(0,e.iD)("div",F,[(0,e._)("h2",null,[(0,e._)("button",{id:"back",onClick:l[12]||(l[12]=t=>{Q.close()})},[G,(0,e.Uk)(" 返回")]),(0,e.Uk)("| 维护单 | 当前运维人员编号："+(0,o.zw)(P.showid)+" | ",1),(0,e._)("button",{id:"add",onClick:l[13]||(l[13]=t=>Q.add())},"添加")]),J,(0,e._)("table",null,[L,(0,e._)("tbody",null,[((0,e.wg)(!0),(0,e.iD)(e.HY,null,(0,e.Ko)(P.content,(t=>((0,e.wg)(),(0,e.iD)("tr",null,[(0,e._)("td",null,(0,o.zw)(t.mreport_id),1),(0,e._)("td",null,(0,o.zw)(t.mreport_date),1),(0,e._)("td",null,(0,o.zw)(t.mreport),1),(0,e._)("td",null,(0,o.zw)(t.device_id_id),1),(0,e._)("td",null,(0,o.zw)(t.staff_id_id),1),(0,e._)("td",null,[(0,e._)("button",{id:"change",onClick:l=>Q.change(t)},"更改",8,N),(0,e.Uk)(" "),(0,e._)("button",{id:"delete",onClick:l=>Q.del(t)},"删除",8,O)])])))),256))])])])):(0,e.kq)("",!0)])])}var Q={data(){return{content:null,device:null,staff:null,detail:null,info:0,showid:0,showAdd:0,showChange:0,mreport_id:"",mreport_date:"",mreport:"",device_id_id:"",staff_id_id:""}},created(){this.getdata()},methods:{getdata(){this.axios.get("http://localhost:8000/api/maintain_view/").then((t=>{this.content=t.data}))},open(t){this.info=1,this.axios.get("http://localhost:8000/api/mreport/query/",{params:{staff_id_id:t}}).then((t=>{this.content=t.data})),this.showid=t,this.axios.get("http://localhost:8000/api/mreport/forkry1/").then((t=>{this.device=t.data})),this.axios.get("http://localhost:8000/api/mreport/forkry2/").then((t=>{this.staff=t.data}))},close(){this.info=0,this.$options.methods.getdata.bind(this)()},add(){this.mreport_date="",this.mreport="",this.device_id_id="",this.showAdd=1},change(t){this.mreport_id=t.mreport_id,this.mreport_date=t.mreport_date,this.mreport=t.mreport,this.device_id_id=t.device_id_id,this.staff_id_id=t.staff_id_id,this.showChange=1},add_commit(){this.showAdd=0,this.axios({method:"post",url:"http://localhost:8000/api/mreport/add/",data:{mreport_date:this.mreport_date,mreport:this.mreport,device_id_id:this.device_id_id,staff_id_id:this.showid},headers:{"Content-Type":"multipart/form-data"}}),setTimeout((()=>{this.$options.methods.open.bind(this)(this.showid)}),100)},change_commit(){this.showChange=0,this.axios({method:"post",url:"http://localhost:8000/api/mreport/update/",data:{mreport_id:this.mreport_id,mreport_date:this.mreport_date,mreport:this.mreport,device_id_id:this.device_id_id,staff_id_id:this.staff_id_id},headers:{"Content-Type":"multipart/form-data"}}),setTimeout((()=>{this.$options.methods.open.bind(this)(this.showid)}),100)},del(t){this.axios({method:"post",url:"http://localhost:8000/api/mreport/delete/",data:{mreport_id:t.mreport_id},headers:{"Content-Type":"multipart/form-data"}}),setTimeout((()=>{this.$options.methods.open.bind(this)(this.showid)}),100)},cancel(){this.showAdd=0,this.showChange=0}}},R=i(89);const S=(0,R.Z)(Q,[["render",P],["__scopeId","data-v-e864be82"]]);var X=S}}]);
//# sourceMappingURL=776.90cb80d8.js.map