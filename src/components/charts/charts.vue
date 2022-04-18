<template>
  <chart-nav v-on:change-chart="changeChart" class="nav-container"/>
  <div class="chart-container">
    <component :is="currentChart"></component>
  </div>
</template>

<script>
import ChartNav from './chartNav.vue'
import TidalVolGraph from './tidalVolGraph.vue'
import FeedVolGraph from './feedVolGraph.vue'
import ReferralsGraph from './referralsGraph.vue'

import store from '@/store/index.js'

export default {
  name: "Charts",
  components: { ChartNav, TidalVolGraph, FeedVolGraph, ReferralsGraph },
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
.chart-container {
  display: flex;
  width: 70vw;
  height: 80vh;
  margin-top: 1vh;
  margin-bottom: 1vh;
}
</style>
