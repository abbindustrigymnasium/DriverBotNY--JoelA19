<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text">
        <span>TheSuperEpicLegoRobotOFSuperMegaEpicness</span>
        
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-content>
      <div >
      
      </div>
    <div >
      <v-btn color="success" v-on:click="Send('f1024')">Forward</v-btn>
      </div>
      <div >
      <v-btn color="success" v-on:click="Send('b1024')">Backward</v-btn>
      </div>
          <div>
            <v-card width="200" height="200" class="test" justify-center> 
            <v-switch v-model="Direction" class="ma-20" label="direction"></v-switch>
      </v-card>
      </div>
    </v-content>
  </v-app>
</template>

<script>
var mqtt = require("mqtt");
import ExampleComp from './components/ExampleComp'
// import VueMqtt from  'vue-mqtt'
export default {
  name: 'App',
  components: {
    ExampleComp,
    
  },
  methods: {
    //Metoder
    Connect() {
      //https://github.com/mqttjs/MQTT.js/blob/master/README.md
      var ref = this;
      if (this.connected == true) {
        return "";
      }
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
  },
  data: () => ({
        counter: 0,
    connected: false,
    client: "JoeDart",
    user: "joel.andersson@abbindustrigymnasium.se",
    pass: "Changes",
  })
}
</script>
