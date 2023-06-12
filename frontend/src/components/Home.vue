<template>
    <div id="main">
      <div id="left">
        <ul>
          <li id="selected"><router-link to="/"><i class="fa fa-home"/>&ensp;首页</router-link></li>
          <li><router-link to="/staff"><i class="fa fa-street-view"/>&ensp;人员</router-link></li>
          <li><router-link to="/area"><i class="fa fa-map-marker"/>&ensp;区域</router-link></li>
          <li><router-link to="/device"><i class="fa fa-wrench"/>&ensp;设备</router-link></li>
          <li><router-link to="/security"><i class="fa fa-shield"/>&ensp;安保系统</router-link></li>
          <li><router-link to="/maintain"><i class="fa fa-archive"/>&ensp;运维系统</router-link></li>
          <li><router-link to="/alarm"><i class="fa fa-bell"/>&ensp;警报处理</router-link></li>
        </ul>
      </div>
      <div id="right">
        <div id="top">
          <ul>
            <li><h1>&ensp;<i class="fa fa-home"/>&ensp;人流量管理系统</h1></li>
          </ul>
          <div style="clear: both;"></div>
        </div>
        <div id="container">
          <br>
            <div id="header">&ensp;<i class="fa fa-user"/>&ensp;全天人流量</div>
            <div id="traffic">
                <div id="traffic1">总人流<br><br>1111</div>
                <div id="traffic2">可视人流<br><br>1111</div>
                <div id="traffic3">入口人流<br><br>1111</div>
                <div id="traffic4">出口人流<br><br>1111</div>
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

      }
    },
    created(){
        this.getdata();
    },
    methods:{
        getdata(){
            this.axios.get('http://localhost:8000/api/query/')
                .then(res=>{
                    this.content=res.data
                });
        },
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
  }
  #header{
    color:#4f4f4f;
    font-size: 30px;
    font-weight: bolder;
  }
  #traffic{
    display: flex;
    color:#4f4f4f;
    font-size: 20px;
    font-weight: bolder;
    text-align: center;
  }
  #traffic1{
    margin: 1em;
    padding: 1em;
    flex:1;
    background-color: rgba(167, 165, 165, 0.3);
  }
  #traffic2{
    margin: 1em;
    padding: 1em;
    flex:1;
    background-color: rgba(167, 165, 165, 0.3);
  }
  #traffic3{
    margin: 1em;
    padding: 1em;
    flex:1;
    background-color: rgba(167, 165, 165, 0.3);
  }
  #traffic4{
    margin: 1em;
    padding: 1em;
    flex:1;
    background-color: rgba(167, 165, 165, 0.3);
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