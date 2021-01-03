<template>
  <div class="main_wrap">
    <div id="nav">
      <div class="logo-wrap">
        <a href="/" class="logo_link">
          <img src="./assets/logo1.png" alt="" class="logo_img">
        </a>
      </div>
      <ul class="main_nav-list">
        <li class="main_nav-item">
          <router-link to="/">Главная</router-link>
        </li>
        <li class="main_nav-item">
          <router-link to="/about">Настройки</router-link>
        </li>
        <li class="main_nav-item">
          <router-link to="/about">Иструкция</router-link>
        </li>
        <li class="main_nav-item">
          <router-link to="/about">Написать нам</router-link>
        </li>
        <li class="main_nav-item">
          <router-link to="/about">О кмопании</router-link>
        </li>
        
      </ul>
    </div>
    <div class="content">
      <router-view/>
    </div>
  </div>
</template>

<style scoped>
  @import 'assets/css/normalizer.css';
  .main_wrap{
    display: grid;
    grid-auto-flow: column;
    grid-template-columns: repeat(10, 1fr);
    min-width: 100vh;
    padding-top: 4em;
    background-color: #1c1f32;
  }
  #nav {
    grid-column: 1/3;
  }
  .main_nav-list {
    height: 100vh;
    list-style: none;
    padding-left: 4em;
    padding-top: 4em;
  }
  .main_nav-item {
    margin-top: 1.5em;
  }
  .main_nav-item > a {
    text-decoration: none;
    color: #6f7c8d
  }
  .content {
    grid-column: 3 / end;
  }
  .logo-wrap{
    text-align: center;
  }
  .logo_link {
    display: block;
    overflow: hidden;
  }
  .logo_img{
    border-radius: 50%;
    height: 5em;
  }
</style>
