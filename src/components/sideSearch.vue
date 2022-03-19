<template>
  <div class="searchContainer">
    <input type="text" placeholder="Search" v-model="search" />
    <ul>
      <li v-for="patient in patients" :key="patient.encounterId">
        <button
          v-bind:class="{
            active: patient.encounterId === currentPatient.encounterId,
          }"
          v-on:click="selectPatient(patient)"
        >
          {{ patient.encounterId }}
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
import store from "@/store/index.js";
export default {
  name: "SideSearch",
  data() {
    return {
      search: "",
    };
  },
  computed: {
    patients() {
      return store.state.patients.filter(
        (patient) => patient.encounterId.indexOf(this.search) !== -1
      );
    },
    currentPatient() {
      return store.state.currentPatient;
    },
  },
  methods: {
    selectPatient(patient) {
      store.commit("setCurrentPatient", patient);
    },
  },
};
</script>
<style scoped>
.searchContainer {
  margin: 0 1vw 0 1vw;
}
ul {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 70vh;
  overflow: scroll;
  list-style: none;
  border: 1px;
  border-style: solid;
  width: 9vw;
  border-width: 3px;
  padding: 0;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
ul::-webkit-scrollbar {
  display: none;
}
input {
  width: 9vw;
  font-size: 20px;
  margin: 1vh 0 0 0;
}

li {
  border-bottom: 1px;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  text-align: center;
  width: 100%;
}
button:hover {
  background: rgb(233, 228, 228);
}
button {
  width: 100%;
  border: none;
  background-color: white;
  font-size: 22px;
}
.active {
  background-color: lightblue;
}
/* Hide scrollbar for Chrome, Safari and Opera */
</style>