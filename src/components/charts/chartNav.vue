<template>
  <div class="nav-container">
    <div class="patient-charts">
      <h2>Current Patient</h2>
      <button v-on:click="changeChart('tidal-vol-graph')">Tidal Volume</button>
      <button v-on:click="changeChart('feed-vol-graph')">Feed Volume</button>
      <button v-on:click="changeChart('feed-vol-graph')">test</button>

    </div>
    <br/>
    <div class="average-charts">
      <h2>Overall Data</h2>
      <button v-on:click="changeChart('referrals-graph')">Referrals</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ChartNav",
  emits: ["changeChart"], 
  methods: {
    changeChart (chart) {
      this.$emit("changeChart", chart)
    }
  },
}
</script>

<style scoped>
.nav-container {
  display: flex;
  flex-direction: column;
  width: 15vw;
  height: 100vh;
}

.average-charts {
  margin-top: 20vh;
}

h2 {
  margin-left: 1vw;
}

button {
  width: 10vw;
  text-align: center;
  padding: 3px;
  margin-left: 1vw;
  margin-bottom: 1vh;
  background-color: lightblue;
  border-color: black;
}
</style>
