<template>
  <div class="header">
    <div class="joinLogo">
      <file-submit />
      <div class="">Logo</div>
    </div>
    <h2 class="name">Name Maybe</h2>
    <button v-on:click="switchContent('patient-info')">Overview</button>
    <button v-on:click="switchContent('graph-slides')">Charts</button>
    <button>
      <router-link to="/report">Generate report</router-link>
    </button>

    <div class="user">
      <button v-if="!user" v-on:click="f">Login</button>
      <p v-else>{{ user }}</p>
    </div>
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

export default {
  name: "home",
  components: { FileSubmit, SideSearch, PatientInfo, GraphSlides },
  data() {
    return {
      user: "",
      currentContent: "graph-slides"
    };
  },
  methods: {
    switchContent: function(component) {
      console.log(component)
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
