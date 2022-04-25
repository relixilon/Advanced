<template>
  <div class="charts-container">
    <div class="nav-container">
      <chart-nav v-on:change-chart="changeChart" class="nav-container"/>
    </div>
    <div class="chart-container">
      <component :is="currentChart"></component>
    </div>
  </div>
</template>

<script>
import ChartNav from './chartNav.vue'
import TidalVolGraph from './tidalVolGraph.vue'
import FeedVolGraph from './feedVolGraph.vue'
import ReferralsGraph from './referralsGraph.vue'
import PeepPipGraph from './peepPipGraph.vue'

import store from '@/store/index.js'

export default {
  name: "Charts",
  components: { ChartNav, 
                TidalVolGraph, 
                FeedVolGraph, 
                ReferralsGraph,
                PeepPipGraph },
  computed: {
    patient() {
      return store.state.currentPatient
    }
  },
  data() {
    return {
      currentChart: ""
    }
  },
  methods: {
    changeChart (chart) {
      this.currentChart = chart
    }
  },  
}
</script>

<style scoped>
.charts-container {
  display: flex;
}

.nav-container {
  display: flex;
  width: 15vw;
  height: 100vh;
}

.chart-container {
  display: flex;
  width: 71vw;
  height: 81vh;
  margin: 1vw;
}
</style>
