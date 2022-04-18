<template>
  <canvas id="ReferralsGraph"></canvas>
</template>

<script>
import Chart from 'chart.js/auto'
import store from '@/store/index.js'

export default {
  name: "ReferralsGraph",
  data() {
    let totalPatients = store.state.patients.length;
    let totalReferred = 0;
    const data = JSON.parse(JSON.stringify(store.state.patients)); 
    for (let i=0; i<totalPatients-1; i++) {
      if (Object.values(data[i])[17] == 1) {
        totalReferred += 1;
      }
    }
    let notReferred = totalPatients - totalReferred
    return {
      notReferred: notReferred,
      totalReferred: totalReferred
    }
  },
  methods: {
    renderReferralGraph() {
      let ctx = document.getElementById('ReferralsGraph').getContext("2d");
      this.referralGraph = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ["Not Referred", "Referred"],
          datasets: [
            {
              data: [this.notReferred, this.totalReferred],
              backgroundColor: ["rgba(21, 100, 255, 0.5)", "rgba(255, 100, 21, 0.5)"],
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
              text: "Referrals",
              color: "black"
            },
            legend: {
              display: true,
            },
          },
        }
      })
    }
  },
  mounted() {
    this.renderReferralGraph();
  }
} 
</script>
