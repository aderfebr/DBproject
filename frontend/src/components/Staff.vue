<template>
  <div id="main">
    <div id="left">
      <ul>
        <li><router-link to="/"><i class="fa fa-home"/>&ensp;首页</router-link></li>
        <li id="selected"><router-link to="/"><i class="fa fa-street-view"/>&ensp;人员</router-link></li>
      </ul>
    </div>
    <div id="right">
      <div id="top">
        <ul>
          <li><h1>&ensp;<i class="fa fa-street-view"/>&ensp;人员</h1></li>
          <li><button id="add">＋</button></li>
        </ul>
        <div style="clear: both;"></div>
      </div>
      <div id="container">
        <br>
        <table>
          <thead>
            <tr>
              <th>字段1</th>
              <th>字段2</th>
              <th>字段3</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1111111</td>
              <td>1111111111</td>
              <td>111111111</td>
              <td><button id="change">更改</button>&ensp;<button id="delete">删除</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

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
  background-color: #28a745;
  color: #fff;
  font-size: 40px;
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
}
a:hover{
  color: #17a2b8;
  transition: all 0.2s;
}
</style>