<template>
  <chart-nav v-on:change-chart="changeChart"/>
  <div class="chart-container">
    <component :is="currentChart"></component>
  </div>
</template>

<script>
import ChartNav from './chartNav.vue'
import TidalVolGraph from './tidalVolGraph.vue'
import FeedVolGraph from './feedVolGraph.vue'

import store from '@/store/index.js'

export default {
  name: "Charts",
  components: { ChartNav, TidalVolGraph, FeedVolGraph },
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

</style>
