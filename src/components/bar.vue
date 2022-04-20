<template>
  <div class="bar">
    <ul>
      <li><button v-on:click="changeComp('patient-info')">Overview</button></li>
      <li><button v-on:click="changeComp('charts')">Charts</button></li>
      <li>
        <button>
          <router-link to="/report"
           style="text-decoration: none;
           color: inherit;">Report</router-link>
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "bar",
  methods: {
    changeComp (component) {
      this.$emit("changeComp", component)
    }
  }
};
</script>

<style scoped>
@import '../assets/variables.css';

.bar {
  display: flex;
  width: 88vw;
  background-color: var(--primary-color);
  height: 5vh;
  align-items: center;
  justify-content: space-between;
}

ul {
  display: flex;
  flex-direction: row;
  list-style: none;
}

button {
  width: 10vw;
  text-align: center;
  padding: 3px;
  margin-left: 1vw;
  background-color: lightblue;
  border-color: black;
}
</style>
