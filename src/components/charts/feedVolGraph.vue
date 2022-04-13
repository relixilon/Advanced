<template>
  <div v-if="feedTotalData == 0">
    <p>Not enough data to generate graph.</p>
  </div>
  <div v-else class="feed-graph-container">
    <canvas id="FeedVolGraph" height="400"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto'
import store from '@/store/index.js'

export default {
  name: 'FeedVolGraph',
  data() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    let feedTotalData = data.feed_vol + data.feed_vol_adm
    return {
      feedTotalData
    }
  },
  mounted() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    let feedVolData = [data.feed_vol, data.feed_vol_adm]
    if (document.getElementById('FeedVolGraph') != null) {
      const ctx = document.getElementById('FeedVolGraph').getContext("2d");
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
    }
    },
  }
</script>

<style scoped>
.feed-graph-container {
  width: 40vw;
  height: 30vh;
  margin-top: 1vh;
  margin-bottom: 1vh;
}

p {
  font-size: 20px;
}
</style>
