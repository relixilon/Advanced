<template>
  <div class="feed-graph-container">
    <canvas id="FeedVolGraph" height="400"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto'
import store from '@/store/index.js'

export default {
  name: 'FeedVolGraph',
  props: {
  },
  mounted() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    const feedVolData = [data.feed_vol, data.feed_vol_adm]

    const ctx = document.getElementById('FeedVolGraph');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ["Feed Vol", "Feed Vol Adm"],
        datasets: [
          {
            data: feedVolData,
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
              }
            },
          xAxes: 
          {
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
.feed-graph-container {
  width: 600px;
  height: 300px;
}
</style>