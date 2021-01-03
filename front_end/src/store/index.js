import { createStore } from 'vuex'

export default createStore({
  state: {
    imageUrl: ['https://sun9-35.userapi.com/impf/t4-PIVbj4lFFne6zpglWYHgHUOPLMNISWUSR9A/2IfUkFIVtv8.jpg?size=1080x1080&quality=96&proxy=1&sign=7b1bb91484153c86b7b7d3363c3b8775&c_uniq_tag=hRU_fI83r9iTSfDgSCkGGR3WaLLKXvN0mIOSJN4tsbo&type=album',
                'https://sun9-41.userapi.com/IZ_aXTL2pB1C1tB7S4Nx7uZD1t-wtRJuHOxl_w/XNZSCV47_AU.jpg',
              'https://sun9-71.userapi.com/impf/yV-w8lLvcXA4gJDOQAmhg6mSXLO4Yir3Lzwwow/IUSWReYDxC0.jpg?size=1280x855&quality=96&proxy=1&sign=74ce00ccc6742a5414c7c8e6e2737b92&c_uniq_tag=3tq3f13s0-RVDL3gFxxMmwlc0E23cgqcr5C3aLouPaM&type=album']
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  },
  getters: {
    getImgUrl: state => {
      return state.imageUrl
    }
  }
})
