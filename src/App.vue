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
      <v-btn color="success">Sucess</v-btn>
    <ExampleComp MSG="apa apa apa" />
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
import ExampleComp from './components/ExampleComp'

export default {
  name: 'App',
  components: {
    ExampleComp
  },
  data () {
    return {
      addnew:false,
      Direction : 1
      //
    }
  }
}
</script>
