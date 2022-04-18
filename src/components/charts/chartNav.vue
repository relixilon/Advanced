<template>
  <div class="nav-container">
    <div class="patient-charts">
      <h2>Current Patient</h2>
      <button v-on:click="changeChart('tidal-vol-graph')">Tidal Volume</button>
      <button v-on:click="changeChart('feed-vol-graph')">Feed Volume</button>
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
button {
  height: 5vh;
  width: 10vw;
}

.nav-container {
  display: flex;
  flex-direction: column;
  width: 15vw;
}

.average-charts {
  border-top: 2px solid;
  margin-top: 20vh;
}

</style>
