<template>
  <div v-if="fio2Data == 0">
    <p>No data to report.</p>
  </div>
  <div v-else>
    <table>
      <tr>
        <th>FiO2</th>
        <th>FiO2 Ratio</th>
        <th>Oxygen Flow Rate</th>
      </tr>
      <tr>
        <td v-if="fio2 == 0">No data</td>
        <td v-else>{{ fio2 }}</td>
        <td v-if="fio2ratio == 0">No data</td>
        <td v-else>{{ fio2ratio }}</td>
        <td v-if="flowrate == 0">No data</td>
        <td v-else>{{ flowrate }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import store from "@/store/index.js";

export default {
  name: 'FioTable',
  data() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    let fio2 = Math.round(data.fio2*100)/100;
    let fio2ratio = Math.round(data.fio2_ratio*100)/100;
    let flowrate = Math.round(data.oxygen_flow_rate*100)/100;
    let fio2Data = fio2 + fio2ratio + flowrate
    return {
      fio2: fio2,
      fio2ratio: fio2ratio,
      flowrate: flowrate,
      fio2Data: fio2Data
    }
  }
}
</script>

<style scoped>
table, td, th {
  border: 1px solid;
  text-align: center;
}

table {
  width: 40vw;
  height: 5vh;
}

p {
  font-size: 20px;
}
</style>
