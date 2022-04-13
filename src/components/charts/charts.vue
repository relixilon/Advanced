<template>
  <p>Graphs go here</p>
  <chart-nav v-on:change-chart="changeChart"/>
  <component :is="currentChart"></component>
</template>

<script>
import ChartNav from './chartNav.vue'
import TidalVolGraph from './tidalVolGraph.vue'
import FeedVolGraph from './feedVolGraph.vue'

export default {
  name: "Charts",
  components: { ChartNav, TidalVolGraph, FeedVolGraph },
  data() {
    return {
      currentChart: "tidal-vol-graph"
    }
  },
  methods: {
    changeChart (chart) {
      this.currentChart = chart
    }
  },  
}
</script>
