<template>
  <div id="main">
    <div id="popAdd" v-if="showAdd">
      <div id="header">&ensp;添加数据</div>
      <div id="body">
        <div style="flex:1;">
          <div>巡视时间<br><input type="text" v-model="sreport_date"></div>
          <div>区域编号<br>
            <select v-model="area_id_id">
              <option v-for="i in area">{{i}}</option>
            </select>
          </div>
        </div>
        <div style="flex:1;">
          <div>巡视描述<br><input type="text" v-model="sreport"></div>
        </div>
      </div>
      <div id="footer">
        <button style="background-color:#28a745;" @click="add_commit()">&ensp;&ensp;&ensp;确认&ensp;&ensp;&ensp;</button>
        <button style="background-color:#dc3545;" @click="cancel()">&ensp;&ensp;&ensp;取消&ensp;&ensp;&ensp;</button>
      </div>
    </div>
    <div id="popAdd" v-if="showChange">
      <div id="header">&ensp;更改数据</div>
      <div id="body">
        <div style="flex:1;">
          <div>巡视单编号<br><input type="text" v-model="sreport_id" readonly="readonly"></div>
          <div>巡视描述<br><input type="text" v-model="sreport"></div>
          <div>员工编号<br>
            <select v-model="staff_id_id">
              <option v-for="i in staff">{{i}}</option>
            </select>
          </div>
        </div>
        <div style="flex:1;">
          <div>巡视时间<br><input type="text" v-model="sreport_date"></div>
          <div>区域编号<br>
            <select v-model="area_id_id">
              <option v-for="i in area">{{i}}</option>
            </select>
          </div>
        </div>
      </div>
      <div id="footer">
        <button style="background-color:#28a745;" @click="change_commit()">&ensp;&ensp;&ensp;确认&ensp;&ensp;&ensp;</button>
        <button style="background-color:#dc3545;" @click="cancel()">&ensp;&ensp;&ensp;取消&ensp;&ensp;&ensp;</button>
      </div>
    </div>
    <div id="left">
      <ul>
        <li><router-link to="/"><i class="fa fa-home"/>&ensp;首页</router-link></li>
        <li><router-link to="/staff"><i class="fa fa-street-view"/>&ensp;人员</router-link></li>
        <li><router-link to="/area"><i class="fa fa-map-marker"/>&ensp;区域</router-link></li>
        <li><router-link to="/device"><i class="fa fa-wrench"/>&ensp;设备</router-link></li>
        <li><router-link to="/security"><i class="fa fa-shield"/>&ensp;安保系统</router-link></li>
        <li id="selected"><router-link to="/maintain"><i class="fa fa-archive"/>&ensp;运维系统</router-link></li>
        <li><router-link to="/alarm"><i class="fa fa-bell"/>&ensp;警报处理</router-link></li>
      </ul>
    </div>
    <div id="right">
      <div id="top">
        <ul>
          <li><h1>&ensp;<i class="fa fa-archive"/>&ensp;运维系统</h1></li>
        </ul>
        <div style="clear: both;"></div>
      </div>
      <div id="container" v-if="!info">
        <br>
        <table>
          <thead>
            <tr>
              <th>员工编号</th>
              <th>加入时间</th>
              <th>姓名</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="i in content">
              <td>{{ i.staff_id }}</td>
              <td>{{ i.join_id }}</td>
              <td>{{ i.name }}</td>
              <td><button id="info" @click="open(i.staff_id)">详情</button></td>
            </tr>
          </tbody>
        </table>
      </div>
      <div id="container" v-if="info">
        <h2><button id="back" @click="close();"><i class="fa fa-arrow-circle-left" />&ensp;返回</button>|&ensp;巡视单&ensp;|&ensp;当前安保人员编号：{{ showid }}&ensp;|&ensp;<button id="add" @click="add()">添加</button></h2>
        <br>
        <table>
          <thead>
            <tr>
              <th>巡视单编号</th>
              <th>巡视时间</th>
              <th>巡视描述</th>
              <th>区域编号</th>
              <th>员工编号</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="i in content">
              <td>{{ i.sreport_id }}</td>
              <td>{{ i.sreport_date }}</td>
              <td>{{ i.sreport }}</td>
              <td>{{ i.area_id_id }}</td>
              <td>{{ i.staff_id_id }}</td>
              <td><button id="change" @click="change(i)">更改</button>&ensp;<button id="delete" @click="del(i)">删除</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default{
  data(){
    return{
      content:null,
      area:null,
      staff:null,
      detail:null,
      info:0,
      showid:0,
      showAdd:0,
      showChange:0,
      sreport_id:"",
      sreport_date:"",
      sreport:"",
      area_id_id:"",
      staff_id_id:"",
    }
  },
  created(){
    this.getdata();
  },
  methods:{
		getdata(){
			this.axios.get('http://localhost:8000/api/security_view/')
			.then(res=>{
				this.content=res.data
			});
		},
    open(i){
      this.info=1;
      this.axios.get('http://localhost:8000/api/report/query/',{
        params:{
          staff_id_id:i,
        }
      })
			.then(res=>{
				this.content=res.data
			});
      this.showid=i;
      this.axios.get('http://localhost:8000/api/report/forkry1/')
			.then(res=>{
				this.area=res.data
			});
      this.axios.get('http://localhost:8000/api/report/forkry2/')
			.then(res=>{
				this.staff=res.data
			});
    },
    close(){
      this.info=0;
      this.$options.methods.getdata.bind(this)();
    },
    add(){
      this.sreport_date="";
      this.sreport="";
      this.area_id_id="",
      this.showAdd=1;
    },
    change(i){
      this.sreport_id=i.sreport_id;
      this.sreport_date=i.sreport_date;
      this.sreport=i.sreport;
      this.area_id_id=i.area_id_id,
      this.staff_id_id=i.staff_id_id,
      this.showChange=1;
    },
    add_commit(){
      this.showAdd=0;
			this.axios({
        method:"post",
        url:"http://localhost:8000/api/report/add/",
        data:{
          sreport_date:this.sreport_date,
          sreport:this.sreport,
          area_id_id:this.area_id_id,
          staff_id_id:this.showid,
        },
        headers: {'Content-Type': 'multipart/form-data'},
      });
      setTimeout(() => {
        this.$options.methods.open.bind(this)(this.showid);
	    }, 100);
    },
    change_commit(){
      this.showChange=0;
			this.axios({
        method:"post",
        url:"http://localhost:8000/api/report/update/",
        data:{
          sreport_id:this.sreport_id,
          sreport_date:this.sreport_date,
          sreport:this.sreport,
          area_id_id:this.area_id_id,
          staff_id_id:this.staff_id_id,
        },
        headers: {'Content-Type': 'multipart/form-data'},
      });
      setTimeout(() => {
        this.$options.methods.open.bind(this)(this.showid);
	    }, 100);
    },
    del(i){
			this.axios({
        method:"post",
        url:"http://localhost:8000/api/report/delete/",
        data:{
          sreport_id:i.sreport_id,
        },
        headers: {'Content-Type': 'multipart/form-data'},
      });
      setTimeout(() => {
        this.$options.methods.open.bind(this)(this.showid);
	    }, 100);
    },
    cancel(){
      this.showAdd=0;
      this.showChange=0;
    }
  }
}
</script>

<style scoped>
#main{
  position: relative;
  top: 5%;
  height: 90%;
  display: flex;
	box-shadow: 0 0 5px rgb(57,167,176),
				      0 0 10px rgb(56,183,145);
}
#popAdd{
  display: flex;
  flex-direction: column;
  position: fixed;
  left: 20%;
  top: 15%;
  width: 60%;
  height: 70%;
  z-index: 3;
  border-radius: 12px;
  background-color: #fff;
}
#popAdd #header{
  width: 100%;
  border-top-left-radius: 12px;
  border-top-right-radius: 12px;
  background-color: rgb(57,167,176);
  color: #fff;
  flex: 3;
  font-size: 30px;
  padding: 50px 0 10px 0;
  border-bottom: 1px solid rgb(177, 176, 176);
}
#popAdd #body{
  flex: 15;
  font-size: 20px;
  padding: 20px;
  display: flex;
}
#popAdd #body input{
  width: 90%;
  margin: 5px;
  height: 25px;
  font-size: 20px;
}
#popAdd #body select{
  width: 92%;
  margin: 5px;
  height: 40px;
  font-size: 20px;
}
#popAdd #footer{
  background-color: #f5f5f5;
  text-align: center;
  flex: 1;
}
#popAdd button{
  color: #fff;
  padding: 10px;
  margin: 20px;
  font-size: 25px;
}
#left{
  flex: 1;
  background-image: linear-gradient(rgba(63, 126, 149, .9),rgba(85, 32, 159, .9));
  box-shadow: 0 0 10px rgb(85, 32, 159);
  z-index: 2;
}
#left li{
  margin: 5%;
  font-size: 25px;
  text-align: center;
  border-radius: 5px;
  list-style: none;
}
li#selected{
  background-color: rgba(0,0,0,.2);
}
#right{
  flex: 7;
  background-color: rgba(255,255,255,.9);
  z-index: 1;
}
#top{
  background-color: rgba(0,0,0,.1);
  box-shadow: 0 5px 10px #888;
}
#top li{
  margin: 1%;
  float: left;
  list-style: none;
}
#container{
  padding: 1%;
  height: 80%;
  overflow-y: scroll;
}
h1{
  font-size: 40px;
  color: #4f4f4f;
}
h2{
  font-size: 25px;
  color: #4f4f4f;
}
table{
  width: 95%;
  margin: auto;
  border-spacing: 0;
  border-collapse: collapse;
}
th{
  padding: 1% 0;
  background-color: #343a40;
  color: white;
}
td{
  padding: 1% 0;
  border: #aaa .5px solid;
  text-align: center;
}
button{
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.2s;
}
button#info{
  padding: 5% 10%;
  background-color: #17a2b8;
  color: #fff;
}
button#back{
  padding: 0% 1%;
  background-color: rgba(0,0,0,0);
  color: #4f4f4f;
  font-weight: bolder;
  font-size: 25px;
}
button#add{
  padding: 0% 1%;
  background-color: #28a745;
  color: #fff;
  font-weight: bolder;
  font-size: 25px;
}
button#change{
  padding: 5% 10%;
  background-color: #ffc107;
  color: #000;
}
button#delete{
  padding: 5% 10%;
  background-color: #dc3545;
  color: #fff;
}
button:hover{
  filter: grayscale(50%);
}
button#back:hover{
  color: #00ddff;
}
a{
  color: white;
  text-decoration: none;
  transition: all 0.2s;
  cursor: pointer;
}
a:hover{
  color: #17a2b8;
  transition: all 0.2s;
}
div::-webkit-scrollbar {
  width: 10px;
}
div::-webkit-scrollbar-thumb {
  border-radius: 10px;
  box-shadow: inset 0 0 5px rgba(0,0,0,0.4);
  background: rgba(0,0,0,0.4);
}
div::-webkit-scrollbar-track {
  box-shadow: inset 0 0 5px rgba(0,0,0,0.4);
  border-radius: 0;
  background: rgba(0,0,0,0.2);
}
input{
  border: 1px solid #ccc;
  padding: 7px 0px;
  border-radius: 3px;
  padding-left:5px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075);
  -webkit-transition: border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s
}
input:focus{
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075),0 0 8px rgba(102,175,233,.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075),0 0 8px rgba(102,175,233,.6)
}
select{
  border: 1px solid #ccc;
  padding: 7px 0px;
  border-radius: 3px;
  padding-left:5px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075);
  -webkit-transition: border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s
}
select:focus{
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075),0 0 8px rgba(102,175,233,.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075),0 0 8px rgba(102,175,233,.6)
}
</style>