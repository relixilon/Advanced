<template>
  <div class="tidal-graph-container">
    <canvas id="TidalVolGraph" height="400"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto'
import store from '@/store/index.js'

export default {
  name: 'TidalVolGraph',
  props: {
  },
  mounted() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    const tidalVolData = [data.tidal_vol, data.tidal_vol_actual]

    const ctx = document.getElementById('TidalVolGraph');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ["Tidal Vol", "Tidal Vol Actual"],
        datasets: [
          {
            data: tidalVolData,
            backgroundColor: "rgba(21, 100, 255, 0.5)",
            borderColor: "#333333",
            borderWidth: 3
          }
        ]
      },
      options: {
        responsiveness: true,
        maintainAspectRatio: false,
        plugins: {
          title: {
            display: true,
            text: "Tidal Volume",
            color: "black"
          },
          legend: {
            display: false,
          }
        },
        scales: {
          yAxes:
            {
              ticks: {
              beginAtZero: true,
              padding: 25,
              color: "black"
              }
            },
          xAxes: {
            ticks: {
              color: "black"
            }
          }
        }
      }
    })
  },
}
</script>

<style scoped>
.tidal-graph-container {
  width: 600px;
  height: 300px;
}
</style>