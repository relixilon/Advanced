
<template>
  <div v-if="peeppipData == 0">
    <p>No data to report.</p>
  </div>
  <div v-else>
    <table>
      <tr>
        <th>Peep</th>
        <th>Pip</th>
      </tr>
      <tr>
        <td v-if="peep == 0">No data</td>
        <td v-else>{{ peep }}</td>
        <td v-if="pip == 0">No data</td>
        <td v-else>{{ pip }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import store from "@/store/index.js";

export default {
  name: 'PeepPipTable',
  data() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    let peep = Math.round(data.fio2*100)/100;
    let pip = Math.round(data.fio2_ratio*100)/100;
    let peeppipData = peep + pip
    return {
      peep: peep,
      pip: pip,
      peeppipData: peeppipData
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
