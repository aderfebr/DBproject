<template>
  <div id="main">
    <div id="left">
      <ul>
        <li id="selected"><router-link to="/wuliao"><i class="fa fa-street-view"/>&ensp;物料表</router-link></li>
        <li><router-link to="/kucun"><i class="fa fa-map-marker"/>&ensp;库存表</router-link></li>
        <li><router-link to="/tiaopei"><i class="fa fa-wrench"/>&ensp;调配构成表</router-link></li>
        <li><router-link to="/mps"><i class="fa fa-shield"/>&ensp;MPS</router-link></li>
        <li><router-link to="/bs"><i class="fa fa-archive"/>&ensp;资产负债表</router-link></li>
      </ul>
    </div>
    <div id="right">
      <div id="top">
        <ul>
          <li><h1>&ensp;<i class="fa fa-street-view"/>&ensp;物料表</h1></li>
        </ul>
        <div style="clear: both;"></div>
      </div>
      <div id="container">
        <br>
        <table>
          <thead>
            <tr>
              <th>物料号</th>
              <th>名称</th>
              <th>单位</th>
              <th>调配方式</th>
              <th>损耗率</th>
              <th>作业提前期</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="i in content">
              <td>{{ i.物料号 }}</td>
              <td>{{ i.名称 }}</td>
              <td>{{ i.单位 }}</td>
              <td>{{ i.调配方式 }}</td>
              <td>{{ i.损耗率 }}</td>
              <td>{{ i.作业提前期 }}</td>
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
      content:null
    }
  },
  created(){
    this.getdata();
  },
  methods:{
		getdata(){
			this.axios.get('http://localhost:8000/api/wuliao/')
			.then(res=>{
				this.content=res.data
			});
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
  padding: 5% 10%;
  cursor: pointer;
  transition: all 0.2s;
}
button#add{
  width: 80px;
  height: 55px;
  background-color: #28a745;
  color: #fff;
  font-size: 25px;
  font-weight: bolder;
}
button#change{
  background-color: #ffc107;
  color: #000;
}
button#delete{
  background-color: #dc3545;
  color: #fff;
}
button:hover{
  filter: grayscale(50%);
}
a{
  color: white;
  text-decoration: none;
  transition: all 0.2s;
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