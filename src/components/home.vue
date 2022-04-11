<template>
  <div class="header">
    <div class="joinLogo">
      <file-submit />
      <div class="">Logo</div>
    </div>
    <h2 class="name">Name Maybe</h2>

    <div class="user">
      <button v-if="!user" v-on:click="f">Login</button>
      <p v-else>{{ user }}</p>
    </div>
  </div>
  
  <div class="nav">
    <bar v-on:change-comp="switchContent"/>
  </div>

  <div class="content">
    <side-search />
    <component :is="currentContent"></component>
  </div>
</template>

<script>
import FileSubmit from "./fileSubmit.vue";
import SideSearch from "./sideSearch.vue";
import PatientInfo from "./patientInfo.vue";
import GraphSlides from "./graphSlides.vue";
import Bar from "./bar.vue";

export default {
  name: "home",
  components: { FileSubmit, SideSearch, Bar, PatientInfo, GraphSlides },
  data() {
    return {
      user: "",
      currentContent: "graph-slides"
    };
  },
  methods: {
    switchContent(component) {
      this.currentContent = component;
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header {
  display: flex;
  flex-direction: row;
  width: 100vw;
  justify-content: space-between;
  align-items: center;
  height: 10vh;
}
.joinLogo {
  display: flex;
  flex-direction: row;
  height: 100%;
  align-items: center;
}
.content {
  display: flex;
}
</style>
