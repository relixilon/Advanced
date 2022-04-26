<template>
  <div class="searchContainer">
    <input class="search" type="text" placeholder="Search" v-model="search" />
    <div class="filter">
      <div>
        Recommended
        <input type="radio" name="filter" value="1" v-model="filter" />
      </div>
      <div>
        Not Recommended
        <input type="radio" name="filter" value="2" v-model="filter" />
      </div>
      <div>
        No data
        <input type="radio" name="filter" value="3" v-model="filter" />
      </div>
      <button v-on:click="resetFilters()" class="reset">reset filters</button>
    </div>

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
      filter: false,
    };
  },
  computed: {
    patients() {
      switch (this.filter) {
        case "1":
          return store.state.patients
            .filter(
              (patient) => patient.encounterId.indexOf(this.search) !== -1
            )
            .filter((patient) => patient["referral\r"] === 1);
        case "2":
          return store.state.patients
            .filter(
              (patient) => patient.encounterId.indexOf(this.search) !== -1
            )
            .filter((patient) => patient["referral\r"] === 0);
        case "3":
          return store.state.patients
            .filter(
              (patient) => patient.encounterId.indexOf(this.search) !== -1
            )
            .filter((patient) => patient["referral\r"] === 3);

        default:
          return store.state.patients.filter(
            (patient) => patient.encounterId.indexOf(this.search) !== -1
          );
      }
    },
    currentPatient() {
      return store.state.currentPatient;
    },
  },
  methods: {
    selectPatient(patient) {
      store.commit("setCurrentPatient", patient);
    },
    resetFilters() {
      this.search = "";
      this.filter = false;
    },
  },
};
</script>
<style scoped>
@import "../assets/variables.css";

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

.search {
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

.filter {
  display: flex;
  flex-direction: column;
  text-align: center;
  height: 4;
  align-items: center;
}

.reset {
  font-size: 15px;
  background-color: var(--secondary-color);
  width: 60%;
}
</style>
