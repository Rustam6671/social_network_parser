<template>
  <div class="home">
    <div class="header">
      <div class="submenu_text-wrapp">
        <h2 class="submenu_text">
          Главная
        </h2>
      </div>
      <div class="user_wrap">
        <button class="user_button">
          <img src="../assets/img/user-photo_162x163.jpg" alt="user photo" class="user_photo">
          <p class="user_text">Ганс Христиан</p>
        </button>
      </div>
    </div>
    <div class="parser_mode">
      <ul class="parser_mode-list">
        <li class="parser_mode-item">
          <a href="#" class="parser_mode-link">
            VK
          </a>
        </li>
        <li class="parser_mode-item">
          <a href="#" class="parser_mode-link">
            INSTAGRAM
          </a>
        </li>
        <li class="parser_mode-item">
          <a href="#" class="parser_mode-link">
            TWITTER
          </a>
        </li>
      </ul>
    </div>
  </div>
  <div class="collection_of_photos">
    <ul class="collection_list">
      <li v-for="imgUrl in listImgUrl" :key="imgUrl.id" class="collection_item">
        <div class="collection_img-wrap">
          <img :src=imgUrl alt="" class="collection_img">
        </div>
        <div class="user_name">Мартынова Светлана</div>
      </li>
    </ul>
  </div>
</template>
<style scoped>
  .header{
    display: grid;
    grid-auto-flow: column;
  }
  .submenu_text{
    font-size: 2.2em;
    margin: 2% 0;
    color:wheat;
  }
  .user_wrap{
    display: grid;
  }
  .user_button{
    background-color: #1c1f32;
    border: none;
    display: grid;
    grid-auto-flow: column;
    
  }
  .user_photo{
    height: 4em;
    border-radius: 50%;
    justify-self: end;
  }
  .user_text {
    justify-self: start;
    color: wheat;
    padding-left: 5%;
    margin: 7% 0;
  }
  .parser_mode-list{
    list-style: none;
    display: grid;
    grid-auto-flow: column;
    grid-template-columns: repeat(7, 1fr);
    text-align: center;
  }
  .parser_mode-link{
    text-decoration: none;
    color: #6f7c8d;
  }
  .collection_list {
    padding: 0;
    margin-left: 2em;
    margin-top: 4em;
    list-style: none;
    display: grid;
    grid-auto-flow: column;
    grid-template-columns: repeat(3, 1fr);
    grid-auto-columns: minmax(auto 10%);


  }
  .collection_img-wrap{
    height:320px;
    width: 200px;
    overflow: hidden;
    text-align: center;
    overflow: hidden;
  }
  .collection_img{
    height: 100%;
    margin-left: -26%;
  }

</style>
<script>
// @ is an alias to /src


export default {
  name: 'Home',
  data() {
    return {
      listImgUrl: []
    }
  },
  components: {
  },
  created() {
    this.receiveImgUrl()
    console.log(this.listImgUrl);
  },
  methods: {
    async receiveImgUrl() {
      this.listImgUrl = this.$store.getters.getImgUrl
    }
    
  }
}
</script>
