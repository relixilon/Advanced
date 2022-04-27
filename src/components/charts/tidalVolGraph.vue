<template>
  <canvas id="TidalVolGraph"></canvas>
</template>

<script>
import Chart from 'chart.js/auto'
import store from '@/store/index.js'

export default {
  name: 'TidalVolGraph',
  watch: {
    tidalData: function() {
      this.tidalGraph.destroy()
      this.renderTidalChart()
    }
  },
  computed: {
    tidalData() {
    let data = JSON.parse(JSON.stringify(store.state.currentPatient));
    let tidalData = [data.tidal_vol, data.tidal_vol_actual]
    return tidalData
    }
  },
  methods: {
    renderTidalChart() {
      let ctx = document.getElementById('TidalVolGraph').getContext("2d");
      this.tidalGraph = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Tidal Vol", "Tidal Vol Actual"],
          datasets: [
            {
              data: this.tidalData,
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
                  },
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
  mounted() {
    this.renderTidalChart();
  }
}
</script>
