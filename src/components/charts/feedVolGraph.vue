<template>
  <div class="feed-graph-container">
    <canvas id="FeedVolGraph"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto'
import store from '@/store/index.js'

export default {
  name: 'FeedVolGraph',
  watch: {
    feedData: function() {
      this.feedGraph.destroy()
      this.renderFeedChart()
    }
  },
  computed: {
    feedData() {
    let data = JSON.parse(JSON.stringify(store.state.currentPatient));
    let feedData = [data.feed_vol, data.feed_vol_adm]
    return feedData
    }
  },
  methods: {
    renderFeedChart() {
      let ctx = document.getElementById('FeedVolGraph').getContext("2d");
      this.feedGraph = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Feed Vol", "Feed Vol Administered"],
          datasets: [
            {
              data: this.feedData,
              backgroundColor: "rgba(255, 100, 21, 0.5)",
              borderColor: "#333333",
              borderWidth: 3
            }
          ]
        },
        options: {
          indexAxis: 'y', 
          responsiveness: true,
          maintainAspectRatio: false,
          animation: {
            duration:0
          },
          plugins: {
            title: {
              display: true,
              text: "Feed Volume",
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
    this.renderFeedChart();
  }
}
</script>

<style scoped>
.feed-graph-container {
  width: 60vw;
  height: 60vh;
  margin-top: 1vh;
  margin-bottom: 1vh;
}
</style>
