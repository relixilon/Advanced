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
@import '../assets/variables.css';

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
  border: 1px solid;
  width: 9vw;
  padding: 0;
  background-color: var(--primary-color);
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}

ul::-webkit-scrollbar {
  display: none;
}

input {
  width: 9vw;
  font-size: 20px;
  margin: 3vh 0 0 0;
}

li {
  border-bottom: 1px solid;
  text-align: center;
  width: 100%;
}

button {
  background-color: var(--primary-color);
}

button:hover {
  background: rgb(233, 228, 228);
}

button {
  width: 100%;
  border: none;
  background-color: var(--primary-color);
  font-size: 22px;
}

.active {
  background-color: var(--secondary-color);
}
</style>
