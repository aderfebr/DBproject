"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[258],{9258:function(t,l,a){a.r(l),a.d(l,{default:function(){return K}});var n=a(3396),e=a(9242),i=a(7139);const d=t=>((0,n.dD)("data-v-409f0040"),t=t(),(0,n.Cn)(),t),o={id:"main"},u={key:0,id:"popAdd"},s=d((()=>(0,n._)("div",{id:"header"}," 添加数据",-1))),_={id:"body"},c={style:{flex:"1"}},r=d((()=>(0,n._)("br",null,null,-1))),h=d((()=>(0,n._)("div",{style:{flex:"1"}},null,-1))),f={id:"footer"},m={id:"left"},p=d((()=>(0,n._)("i",{class:"fa fa-street-view"},null,-1))),w=d((()=>(0,n._)("i",{class:"fa fa-map-marker"},null,-1))),b=d((()=>(0,n._)("i",{class:"fa fa-wrench"},null,-1))),k=d((()=>(0,n._)("i",{class:"fa fa-shield"},null,-1))),v={id:"selected"},g=d((()=>(0,n._)("i",{class:"fa fa-archive"},null,-1))),y={id:"right"},U={id:"top"},C=d((()=>(0,n._)("li",null,[(0,n._)("h1",null,[(0,n.Uk)(" "),(0,n._)("i",{class:"fa fa-archive"}),(0,n.Uk)(" 资产负债表查询")])],-1))),W=d((()=>(0,n._)("button",{id:"clear"},"返回",-1))),x=d((()=>(0,n._)("button",{id:"answer"},"计算",-1))),A=d((()=>(0,n._)("div",{style:{clear:"both"}},null,-1))),D={id:"container"},T=d((()=>(0,n._)("br",null,null,-1))),q=d((()=>(0,n._)("thead",null,[(0,n._)("tr",null,[(0,n._)("th",null,"变量名")])],-1)));function $(t,l,a,d,$,z){const H=(0,n.up)("router-link");return(0,n.wg)(),(0,n.iD)("div",o,[$.showAdd?((0,n.wg)(),(0,n.iD)("div",u,[s,(0,n._)("div",_,[(0,n._)("div",c,[(0,n._)("div",null,[(0,n.Uk)("变量名"),r,(0,n.wy)((0,n._)("input",{type:"text","onUpdate:modelValue":l[0]||(l[0]=t=>$.name=t)},null,512),[[e.nr,$.name]])])]),h]),(0,n._)("div",f,[(0,n._)("button",{style:{"background-color":"#28a745"},onClick:l[1]||(l[1]=t=>z.add_commit())},"   确认   "),(0,n._)("button",{style:{"background-color":"#dc3545"},onClick:l[2]||(l[2]=t=>z.cancel())},"   取消   ")])])):(0,n.kq)("",!0),(0,n._)("div",m,[(0,n._)("ul",null,[(0,n._)("li",null,[(0,n.Wm)(H,{to:"/wuliao"},{default:(0,n.w5)((()=>[p,(0,n.Uk)(" 物料表")])),_:1})]),(0,n._)("li",null,[(0,n.Wm)(H,{to:"/kucun"},{default:(0,n.w5)((()=>[w,(0,n.Uk)(" 库存表")])),_:1})]),(0,n._)("li",null,[(0,n.Wm)(H,{to:"/tiaopei"},{default:(0,n.w5)((()=>[b,(0,n.Uk)(" 调配构成表")])),_:1})]),(0,n._)("li",null,[(0,n.Wm)(H,{to:"/mps"},{default:(0,n.w5)((()=>[k,(0,n.Uk)(" MPS")])),_:1})]),(0,n._)("li",v,[(0,n.Wm)(H,{to:"/bs"},{default:(0,n.w5)((()=>[g,(0,n.Uk)(" 资产负债表")])),_:1})])])]),(0,n._)("div",y,[(0,n._)("div",U,[(0,n._)("ul",null,[C,(0,n._)("li",null,[(0,n.Wm)(H,{to:"/bs"},{default:(0,n.w5)((()=>[W])),_:1})]),(0,n._)("li",null,[(0,n._)("button",{id:"add",onClick:l[3]||(l[3]=t=>z.add())},"添加")]),(0,n._)("li",null,[(0,n._)("button",{id:"clear",onClick:l[4]||(l[4]=t=>z.clear())},"清空")]),(0,n._)("li",null,[(0,n.Wm)(H,{to:"/answer_bs"},{default:(0,n.w5)((()=>[x])),_:1})])]),A]),(0,n._)("div",D,[T,(0,n._)("table",null,[q,(0,n._)("tbody",null,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)($.content,(t=>((0,n.wg)(),(0,n.iD)("tr",null,[(0,n._)("td",null,(0,i.zw)(t.变量名),1)])))),256))])])])])])}var z={data(){return{content:null,showAdd:0,name:""}},created(){this.getdata()},methods:{getdata(){this.axios.get("http://localhost:8000/api/query_bs/").then((t=>{this.content=t.data}))},add(){this.name="",this.showAdd=1},add_commit(){this.showAdd=0,this.axios({method:"post",url:"http://localhost:8000/api/add_bs/",data:{name:this.name},headers:{"Content-Type":"multipart/form-data"}}),setTimeout((()=>{this.$options.methods.getdata.bind(this)()}),100)},cancel(){this.showAdd=0},clear(){this.axios.get("http://localhost:8000/api/clear_bs/").then((t=>{this.content=t.data})),setTimeout((()=>{this.$options.methods.getdata.bind(this)()}),100)}}},H=a(89);const I=(0,H.Z)(z,[["render",$],["__scopeId","data-v-409f0040"]]);var K=I}}]);
//# sourceMappingURL=258.415c0094.js.map