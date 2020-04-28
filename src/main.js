import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'


import store from './store/store'


new Vue({
  render: h => h(App),
  
  store,
  methods: {
    //Metoder
    Connect() {
      //https://github.com/mqttjs/MQTT.js/blob/master/README.md
      var ref = this;
      if (this.connected == true) {
        return "";
      }
      let User = this.$store.getters.GetUser;
      this.clientId =
        "DriverControll" +
        Math.random()
          .toString(16)
          .substr(2, 8);
      var mqtt_url = "joel.andersson@abbindustrigymnasium.se"
      var url = "mqtt://" + mqtt_url;
      var options = {
        port: 8883,
        clientId: this.clientId,
        username: "joel.andersson@abbindustrigymnasium.se",
        password: "Changes"
      };
      this.options = options;
      // console.log("connecting");
      this.client = mqtt.connect(url, options);
      // console.log("connected?");
      this.client
        .on("connect", function() {
          // console.log("success");
          ref.Connecting(true);
        })
        .on("error", function() {
          // console.log("error");
          ref.Connecting(false);
        })
        .on("close", function() {
          ref.Connecting(false);
          // console.log("closing");
        });
    },
    Connecting(connected) {
      this.connected = connected;
      this.$store.dispatch("Connect", connected);
      // console.log(this.connected)
      if (connected == false) {
        this.car = "red";
      } else {
        this.car = "blue";
        this.Send("drive", this.clientId + " har anslutits.");
      }
    },
    Send(adress, message) {
      // console.log(message);
      this.client.publish(
        this.options.username + "/" + "drive", //Exempel         "joakim.flink@abbindustrigymnasium.se"+"/" + "drive",
        message
      );
      this.$store.dispatch("addToLogger", message);
    }
  }
  //   clickSub: function() {
  //       this.$mqtt.subscribe('joel.andersson@abbindsutrigymnasium.se/drive')
  //   },
  //   clickPub: function(val) {
  //       this.$mqtt.publish('joel.andersson@abbindustrigymnasium.se/drive', val)
  //   },

  }

).$mount('#app')
