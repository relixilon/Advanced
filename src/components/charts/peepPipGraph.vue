<template>
  <canvas id="PeepPipGraph"></canvas>
</template>

<script>
import Chart from 'chart.js/auto'
import store from '@/store/index.js'

export default {
  name: 'PeepPipGraph',
  watch: {
    peepPipData: function() {
      this.peepPipGraph.destroy()
      this.renderPeepPipChart()
    }
  },
  computed: {
    peepPipData() {
    let data = JSON.parse(JSON.stringify(store.state.currentPatient));
    let peepPipData = [data.peep, data.pip]
    return peepPipData
    }
  },
  methods: {
    renderPeepPipChart() {
      let ctx = document.getElementById('PeepPipGraph').getContext("2d");
      this.peepPipGraph = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Peep", "Pip"],
          datasets: [
            {
              data: this.peepPipData,
              backgroundColor: "rgba(147, 250, 165, 0.5)",
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
              text: "Peep/Pip",
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
    this.renderPeepPipChart();
  }
}
</script>
