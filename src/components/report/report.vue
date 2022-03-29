<template>
  <div class="report-container">

    <div class="button-container">
      <button><router-link to="/">Home</router-link></button>
      <button><a href="">Download as PDF</a></button>
      <router-view/>
    </div>

    <div class="chart-info-container">
      <chart-info/>
    </div>

    <br/>

    <div class="referred-container">
      <p v-if="referral == 1">PATIENT HAS BEEN FLAGGED FOR REFERRAL</p>
      <p v-if="referral == 0">PATIENT HAS NOT BEEN FLAGGED FOR REFERRAL</p>
    </div>

    <div class="bmi-container">
      <h2>Body Mass Index</h2>
      <p>BMI's over 30 and under 18 indicate patient is in dangerous range.</p>
      <p v-if="bmi == 0" class="bmi-value">No BMI data for patient</p>
      <p v-else class="bmi-value">Patient BMI: {{ bmi }}</p>
    </div>

    <div class="tidal-vol-container">
      <h2>Lung Capacity</h2>
      <p>A healthy adult male has a tidal volume of around 500, females around 400.</p>
      <tidal-vol-table/>
      <tidal-vol-graph/>
    </div>

    <div class="feed-vol-container">
      <h2>Feeding Volume</h2>
      <p>Tracking of tube feeding administered to patient.</p>
      <feed-vol-table/>
      <feed-vol-graph/>
    </div>
    <div class="other-info-container">
        <h2>Other Information</h2>
    </div>
    <br/>
    <div class="footer-container">
      <more-info/>
    </div>
  </div>
</template>

<script>
import store from "@/store/index.js";
import ChartInfo from "./chartInfo.vue"

import TidalVolTable from "./tables/tidalVolTable.vue"
import TidalVolGraph from "./graphs/tidalVolGraph.vue"

import FeedVolTable from "./tables/feedVolTable.vue"
import FeedVolGraph from "./graphs/feedVolGraph.vue"

import MoreInfo from "./moreInfo.vue"

export default {
  name: "Report",
  components: { ChartInfo,
                TidalVolGraph,
                FeedVolGraph,
                TidalVolTable,
                FeedVolTable,
                MoreInfo
                },
  data() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));

    // Get referral (1=referred, 0=no referral)
    let referral = Object.values(data)[17]
    // Get bmi and generate only first 2 decimals
    let bmi = Math.round(data.bmi*100)/100;
    return {
      bmi: bmi,
      referral: referral
    }
  }
}
</script>

<style scoped>
.report-container {
  margin-left: 10%;
  margin-right: 10%;
  padding-left: 20px;
  padding-right: 20px;
  border-left: 2px solid;
  border-right: 2px solid;
  background-color: #d0d0d0;
}

.button-container {
  padding-top: 20px;
  padding-bottom: 20px;
}

a {
  text-decoration: none;
  color: black;
}

button {
  margin-right: 15px;
  font-size: 15px;
  text-align: center;
  background-color: lightblue;
  padding: 5px;
  border-color: black;
}

h2 {
  margin: 0;
  margin-top: 20px;
  margin-bottom: 10px;
}

p {
  margin: 0;
}

.bmi-value {
  font-size: 20px;
}

.chart-info-container {
  border-top: 2px solid;
  border-bottom: 2px solid;
}

.referred-container {
  font-size: 20px;
}
</style>