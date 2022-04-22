<template>
  <div class="report-container">

    <div class="button-container">
      <button><router-link to="/">Home</router-link></button>
    </div>

    <div class="chart-info-container">
      <chart-info/>
    </div>

    <br/>

    <div v-if="encounterId == undefined" class="no-patient-container">
      <p>No patient selected, could not generate report.</p>
    </div>

    <div v-else>
      <div class="referred-container">
        <p v-if="referral == 1">PATIENT HAS BEEN FLAGGED FOR REFERRAL</p>
        <p v-else>PATIENT HAS NOT BEEN FLAGGED FOR REFERRAL</p>
      </div>

      <div class="bmi-container">
        <h2>Body Mass Index</h2>
        <p>BMI's over 30 and under 18 indicate patient is in dangerous range.</p>
        <p v-if="bmi == 0" class="patient-data">No BMI data for patient</p>
        <p v-else class="patient-data">Patient BMI: {{ bmi }}</p>
      </div>

      <div class="tidal-vol-container">
        <h2>Lung Capacity</h2>
        <p>A healthy adult male has a tidal volume of around 500, females around 400.</p>
        <tidal-vol-table/>
        <div class="chart-container">
          <tidal-vol-graph/>
        </div>
      </div>

      <div class="fio2-container">
        <h2>FiO2 and Oxygen Flow Rate</h2>
        <p>Amount of oxygen delievered to patient. Room air is 21% O2.</p>
        <fio-table/>
      </div>

      <div class="feed-vol-container">
        <h2>Feeding Volume</h2>
        <p>Tracking of tube feeding administered to patient.</p>
        <feed-vol-table/>
        <div class="chart-container">
          <feed-vol-graph/>
        </div>
      </div>

      <div class="other-info-container">
          <h2>Other Information</h2>
      </div>

      <br/>
      <footer>
        <more-info/>
      </footer>
    </div>
  </div>
</template>

<script>
import store from "@/store/index.js";
import ChartInfo from "./chartInfo.vue"

import FioTable from "./tables/fio2Table.vue"
import FeedVolTable from "./tables/feedVolTable.vue"
import TidalVolTable from "./tables/tidalVolTable.vue"

import FeedVolGraph from "../charts/feedVolGraph.vue"
import TidalVolGraph from "../charts/tidalVolGraph.vue"

import MoreInfo from "./moreInfo.vue"

export default {
  name: "Report",
  components: { ChartInfo,
                TidalVolGraph,
                FeedVolGraph,
                FioTable,
                TidalVolTable,
                FeedVolTable,
                MoreInfo
                },
  data() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    let encounterId = data.encounterId
    // Get referral (1=referred, 0=no referral)
    let referral = Object.values(data)[17]
    // Get bmi and generate only first 2 decimals
    let bmi = Math.round(data.bmi*100)/100;
    return {
      bmi: bmi,
      referral: referral,
      encounterId: encounterId
    }
  }
}
</script>

<style scoped>
.report-container {
  display: flex;
  flex-wrap: wrap;
  margin-left: 10vw;
  margin-right: 10vw;
  border-left: 2px solid;
  border-right: 2px solid;
  background-color: #d0d0d0;
}

.button-container, .chart-info-container, .referred-container, .bmi-container,
.tidal-vol-container, .feed-vol-container, .other-info-container, .no-patient-container, 
.fio2-container, footer {
  flex-direction: row;
  width: 80vw;
  margin-left: 1vw;
  margin-right: 1vw;
}

.chart-info-container {
  margin-top: 2vh;
  border-top: 2px solid;
  border-bottom: 2px solid;
}

.referred-container, .patient-data {
  font-size: 20px;
}

.chart-container {
  width: 40vw;
  height: 30vh;
  margin-top: 1vh;
  margin-bottom: 1vh;
}

button {
  margin-top: 1vh;
  margin-right: 15px;
  font-size: 15px;
  text-align: center;
  padding: 5px;
  background-color: lightblue;
  border-color: black;
}

a {
  text-decoration: none;
  color: black;
}

p, h2 {
  margin-top: 1vh;
  margin-bottom: 1vh;
}

footer {
  font-size: 13px;
}
</style>
