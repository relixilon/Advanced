<template>
  <div class="home-container">
    <div class="side-bar-container">
      <div class="file-submit">
        <file-submit />
      </div>
      <div class="side-search">
        <side-search />
      </div>
    </div>

    <div class="main-container">
      <div class="header">
        <div class="logo">
          <img src="../assets/MOSA_Healthcare-logos_black.png" />
        </div>
        <div class="title">
          <h2>MOSA Dashboard</h2>
        </div>
        <h2 v-if="user" class="user">User: {{ user }}</h2>
      </div>

      <div class="nav-container">
        <bar v-on:change-comp="switchContent" />
      </div>

      <div class="content-container">
        <component :is="currentContent"></component>
      </div>
    </div>
  </div>
</template>

<script>
import FileSubmit from "./fileSubmit.vue";
import SideSearch from "./sideSearch.vue";
import PatientInfo from "./patientInfo.vue";
import Charts from "./charts/charts.vue";
import Bar from "./bar.vue";
import store from "../store/index";
export default {
  name: "home",
  components: { FileSubmit, SideSearch, Bar, PatientInfo, Charts },
  data() {
    return {
      currentContent: "patient-info",
    };
  },
  computed: {
    loginState() {
      return store.state.loginState;
    },
    user() {
      return store.state.user;
    },
  },
  methods: {
    switchContent(component) {
      this.currentContent = component;
    },
  },
};
</script>

<style scoped>
@import "../assets/variables.css";

.home-container {
  display: flex;
  width: 100vw;
  background-color: var(--secondary-color);
}

.side-bar-container {
  display: flex;
  flex-direction: column;
  width: 12vw;
  height: 100vh;
  background-color: var(--primary-color);
}

.file-submit {
  height: 10vh;
  border-bottom: 1px solid;
  border-right: 1px solid;
}

img {
  height: 10vh;
  width: 20vw;
}

.side-search {
  height: 100vh;
  border-right: 1px solid;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px 4px 6px,
    rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
}

.header {
  display: flex;
  height: 10vh;
  flex-direction: row;
  border-bottom: 1px solid;
  background-color: var(--secondary-color);
}

.logo {
  height: 10vh;
  width: 20vw;
  border-right: 1px solid;
}

.title {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 60vw;
  height: 10vh;
  background-color: var(--secondary-color);
}
.nav-container {
  border-bottom: 1px solid;
  box-shadow: rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px,
    rgba(0, 0, 0, 0.09) 0px -3px 5px;
  background-color: var(--primary-color);
}

.content-container {
  width: 88vw;
  height: 80vh;
}
</style>
