<template>
  <div id="main">
    <div id="left">
      <ul>
        <li><router-link to="/item"><i class="fa fa-street-view"/>&ensp;商品</router-link></li>
        <li><router-link to="/order"><i class="fa fa-map-marker"/>&ensp;订单</router-link></li>
        <li id="selected"><router-link to="/crm"><i class="fa fa-wrench"/>&ensp;推荐系统</router-link></li>
      </ul>
    </div>
    <div id="right">
      <div id="top">
        <ul>
          <li><h1>&ensp;<i class="fa fa-wrench"/>&ensp;推荐系统</h1></li>
        </ul>
        <div style="clear: both;"></div>
      </div>
      <div id="container">
        <div id="list" v-for="i in content">
          <img :src="require('./img/'+i.item_id+'.png')">
          <ul>
            <li><button id="info">商品编号</button>&ensp;{{ i.item_id }}</li>
            <li><button id="info">商品名称</button>&ensp;{{ i.item_name }}</li>
            <li><button id="info">价格</button>&ensp;{{ i.price }}</li>
            <li><button id="info">简介</button>&ensp;{{ i.info }}</li>
          </ul>
          <div id="go"><router-link to="/crm"><button id="add">返回</button></router-link></div>
        </div>
        <div id="recommend">
          <div id="re_left">
            <button id="title">根据最近邻算法为您推荐：</button>
            <div v-for="i in knn" id="re_content"><img :src="require('./img/'+i[0]+'.png')"><br><br><div></div><button id="info" @click="refresh()"><router-link :to="{path:'/answer',query:{id:i[0]}}">{{ i[1] }}</router-link></button></div>
          </div>
          <div id="re_right">
            <button id="title">根据Apriori算法为您推荐：</button>
            <div v-for="i in apriori" id="re_content"><img :src="require('./img/'+i[0]+'.png')"><br><br><div></div><button id="info" @click="refresh()"><router-link :to="{path:'/answer',query:{id:i[0]}}">{{ i[1] }}</router-link></button></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default{
  data(){
    return{
      content:null,
      knn:null,
      apriori:null
    }
  },
  created(){
    this.getdata();
    this.getknn();
    this.getapriori();
  },

  methods:{
    refresh(){
      this.$router.go(0)
    },
		getdata(){
			this.axios.get('http://localhost:8000/api/items/',{
        params:{
          id:this.$route.query.id,
        }
      })
			.then(res=>{
				this.content=res.data
			});
		},
		getknn(){
			this.axios.get('http://localhost:8000/api/knn/',{
        params:{
          id:this.$route.query.id,
        }
      })
			.then(res=>{
				this.knn=res.data
			});
		},
    getapriori(){
			this.axios.get('http://localhost:8000/api/apriori/',{
        params:{
          id:this.$route.query.id,
        }
      })
			.then(res=>{
				this.apriori=res.data
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
#list{
  height: 250px;
  display: flex;
  margin: 3%;
}
#list img{
  flex: 1;
  margin: 1%;
}
#list ul{
  text-align: left;
  flex: 3;
  margin: 1%;
  padding: 1%;
  list-style: none;
  box-shadow: 0 5px 10px #888;
  border-radius: 5px;
  background-color: rgba(0,0,0,.1);
}
#list li{
  padding: .25em;
}
#go{
  margin: 1%;
  padding: 1%;
  flex: .25;
}
#recommend{
  border-top: #aaa 1px solid;
  display: flex;
  text-align: center;
  margin: 5%;
}
#re_left{
  flex: 1;
  padding: 3%;
}
#re_right{
  flex: 1;
  padding: 3%;
}
#re_content{
  margin: 5%;
}
img{
  box-shadow: 0 5px 10px #888;
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
button#info{
  border: none;
  padding: 10px;
  border-radius: 5px;
  font-weight: bolder;
  background-color: #343a40;
  color: #fff;
}
button#add{
  border: none;
  padding: 15px;
  border-radius: 10px;
  background-color: #dc3545;
  box-shadow: 0 5px 10px #888;
  color: #fff;
  width: 50px;
  height: 200px;
  font-size: 18px;
}
button#add:hover{
  filter: grayscale(50%);
  cursor: pointer;
}
button#title{
  border: none;
  color: #000;
  font-size: 18px;
  font-weight: bolder;
  background-color: rgba(0,0,0,0);;
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