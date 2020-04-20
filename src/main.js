import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'


import store from './store/store'


new Vue({
  render: h => h(App),
  
  store,
  methods: {
    clickSub: function(val) {
        this.$mqtt.subscribe('joel.andersson@abbindsutrigymnasium.se')
    },
    clickPub: function(val) {
        this.$mqtt.publish('joel.andersson@abbindustrigymnasium.se/drive', '1024')
    }
  }

}).$mount('#app')
