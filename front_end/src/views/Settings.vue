<template>
  <form id="app">
    <label for="hashtag">Введите хэштег</label>
    <input id="hashtag" v-model="hashtag" type="text">
    <input type="submit" value="Отправить" @click="findByHashtag()">
  </form>
</template>

<script>
export default {
name: 'Settings',
  data() {
      return {
          hashtag: ''
      }
  },
  components: {
  },
  created() {
  },
  methods: {
      async findByHashtag() {
          let data = {
              hashtag: this.hashtag
          }
          fetch('http://localhost:8081/find_photo_and_remember/',
          {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json'
              },
              body: JSON.stringify(data)
          }).then(response => {
              console.log(response.json());
          })
      }
  }
}
</script>

<style>

</style>