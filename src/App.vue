<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text">
        <!-- Titeln på toppen av webbsidan -->
        <span>TheSuperEpicLegoRobotOfSuperMegaEpicness</span> 
        
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-content>
      <div >
      
      </div>
    <div >
      <!-- alla knappar -->
      <!-- använder send() funktionen för att skicka det meddelande som hänger ihop med knappen -->
      <v-btn color="success" v-on:click="direc='f'; Send(direc + '1024' + ang)">Forward</v-btn> 
      </div>
      <div >
      <v-btn color="success" v-on:click="direc='b'; Send(direc + '1024' + ang)">Backward</v-btn>
      </div>
      <div >
      <v-btn color="success" v-on:click="direc='b'; Send(direc + '0000' + ang)">Stop</v-btn>
      </div>
          <div>
            <!-- till skillnad från de andra knapparna ändrar de här bara ang, alltså vilken riktning som bilen svänger åt -->
            <!-- detta system låter mig styra om bilen kör framåt eller bakåt och åt vilket håll den svänger separat -->
            <v-card width="200" height="200" class="test" justify-center> 
            <v-btn color="success" v-on:click="ang='000'; Send(direc + '1024' + ang)">Left</v-btn>
            <v-btn color="success" v-on:click="ang='180'; Send(direc + '1024' + ang)">Right</v-btn>
            <v-btn color="success" v-on:click="ang='090'; Send(direc + '1024' + ang)">Mid</v-btn>
      </v-card>
      </div>
    </v-content>
  </v-app>
</template>

<script>
var mqtt = require("mqtt");
// import VueMqtt from  'vue-mqtt'
export default {
  created() {
    this.connect();
    this.Send("f1024090");
  },
  name: 'App',
  methods: {
    //Funktionen för att koppla till MQTT
   connect() {
      var mqtt_url = "maqiatto.com";
      var url = "mqtt://" + mqtt_url;
      var options = {
        port: 8883,
        clientId:
          "mqttjs_" +
          Math.random()
            .toString(16)
            .substr(2, 8),
        username: this.user,
        password: this.pass
      };
      // user = this.options.username
      // pass = this.options.password
      /* eslint-disable */
      console.log("connecting");
      this.client = mqtt.connect(url, options);
      /* eslint-disable */
      console.log("connected?");
      this.client
        .on("error", function(error) {
          /* eslint-disable */
          console.log("no");
          this.connected = false;
          /* eslint-disable */
          console.log(this.connected);
        })
        .on("close", function(error) {
          /* eslint-disable */
          console.log("no");
          this.connected = false;
        });
      this.connected = true;
    },
    Connecting(connected) {
      this.connected = connected;
      this.$store.dispatch("Connect", connected);
      // console.log(this.connected)
      if (connected == true) {
        this.Send("drive", this.clientId + " har anslutits.");
      }
    }, // funktionen som faktiskt skickar alla meddelanden
    Send(message) {
      this.client.publish("joel.andersson@abbindustrigymnasium.se/drive", message);
      // console.log så att jag kan se att funkar utan att behöva sättta på arduinon
     console.log(message);
    },
  },// data
  data: () => ({
    ang: "090",
    direc: "f",
    connected: false,
    client: "JoeDart",
    user: "joel.andersson@abbindustrigymnasium.se",
    pass: "Changes",
  })
}
</script>
