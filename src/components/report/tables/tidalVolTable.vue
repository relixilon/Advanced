<template>
  <div v-if="tidalData == 0">
    <p>No data to report.</p>
  </div>
  <div v-else>
    <table>
      <tr>
        <th>Tidal Vol</th>
        <th>Tidal Vol Actual</th>
        <th>Tidal Vol KG</th>
        <th>Tidal Vol Spon</th>
        <th>End Tidal CO2</th>
      </tr>
      <tr>
        <td v-if="tidalVol == 0">No data</td>
        <td v-else>{{ tidalVol }}</td>
        <td v-if="tidalVolActual == 0">No data</td>
        <td v-else>{{ tidalVolActual }}</td>
        <td v-if="tidalVolKg == 0">No data</td>
        <td v-else>{{ tidalVolKg }}</td>
        <td v-if="tidalVolSpon == 0">No data</td>
        <td v-else>{{ tidalVolSpon }}</td>
        <td v-if="tidalCO2 == 0">No data</td>
        <td v-else>{{ tidalCO2 }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import store from "@/store/index.js";

export default {
  name: 'TidalVolTable',
  data() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    // Only generate first 2 decimals
    let tidalVol = Math.round(data.tidal_vol*100)/100;
    let tidalVolActual = Math.round(data.tidal_vol_actual*100)/100;
    let tidalVolKg = Math.round(data.tidal_vol_kg*100)/100;
    let tidalVolSpon = Math.round(data.tidal_vol_spon*100)/100;
    let tidalCO2 = Math.round(data.end_tidal_co2*100)/100;

    let tidalData = tidalVol + tidalVolActual + tidalVolKg + tidalVolSpon + tidalCO2

    return {
      tidalVol: tidalVol,
      tidalVolActual: tidalVolActual,
      tidalVolKg: tidalVolKg,
      tidalVolSpon: tidalVolSpon,
      tidalCO2: tidalCO2,
      tidalData: tidalData
    }
  }
}
</script>

<style scoped>
table, th, td {
  border: 1px solid;
  text-align: center;
}

table {
  width: 40vw;
  height: 5vh;
}
</style>