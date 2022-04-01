<template>
  <div v-if="tidalTotalData == 0">
    <p>Not enough data to generate graph.</p>
  </div>
  <div v-else class="tidal-graph-container">
    <canvas id="TidalVolGraph" height="400"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto'
import store from '@/store/index.js'

export default {
  name: 'TidalVolGraph',
  data() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    let tidalTotalData = data.tidal_vol + data.tidal_vol_actual
    return {
      tidalTotalData
    }
  },
  mounted() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    let tidalVolData = [data.tidal_vol, data.tidal_vol_actual];
    if (document.getElementById('TidalVolGraph') != null) {
      const ctx = document.getElementById('TidalVolGraph').getContext("2d");
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
          animation: {
            duration:0
          },
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
    }
    },
  }
</script>

<style scoped>
.tidal-graph-container {
  width: 40vw;
  height: 30vh;
  margin-top: 1vh;
  margin-bottom: 1vh;
}

p {
  font-size: 20px;
}
</style>