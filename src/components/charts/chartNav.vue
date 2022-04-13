<template>
  <button v-on:click="changeChart('tidal-vol-graph')">Tidal Volume</button>
  <button v-on:click="changeChart('feed-vol-graph')">Feed Volume</button>
</template>

<script>
export default {
  name: "ChartNav",
  methods: {
    changeChart (chart) {
      this.$emit("changeChart", chart)
    }
  },
}
</script>

<style scoped>
button {
  height: 10vh;
}
</style>
