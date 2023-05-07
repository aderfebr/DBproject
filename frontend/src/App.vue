<template>
  <div id="bg">
    <vue-particles
        color="#dedede"
        :particleOpacity="0.7"
        :particlesNumber="80"
        shapeType="edge"
        :particleSize="4"
        linesColor="#dedede"
        :linesWidth="1"
        :lineLinked="true"
        :lineOpacity="0.4"
        :linesDistance="150"
        :moveSpeed="2"
        :hoverEffect="true"
        hoverMode="grab"
        :clickEffect="false"
        clickMode="push"
      >
    </vue-particles>
    <RouterView></RouterView>
  </div>
</template>

<script>

</script>

<style>
*{
    padding: 0;
    margin: 0;
}
#bg{
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    background: linear-gradient(120deg,#2871fa,#330d69);
    background-size: 500%;
    animation: bgmovement 60s linear infinite;
}
#particles-js{
    width: 100%;
    height: 100%;
    position: absolute;
    overflow: hidden;
}
@keyframes bgmovement{
    0%,100%{
        background-position: 0% 50%;
    }
    50%{
        background-position: 100% 50%;
    }
}
</style>
