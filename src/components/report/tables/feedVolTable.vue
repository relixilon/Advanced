<template>
  <div v-if="feedingData == 0">
    <p>No data to report.</p>
  </div>
  <div v-else>
    <table>
      <tr>
        <th>Feeding Vol</th>
        <th>Feeding Vol Administered</th>
      </tr>
      <tr>
        <td v-if="feedingVol == 0">No data</td>
        <td v-else>{{ feedingVol }}</td>
        <td v-if="feedingVolAdm == 0">No data</td>
        <td v-else>{{ feedingVolAdm }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import store from "@/store/index.js";

export default {
  name: 'FeedVolTable',
  data() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    let feedingVol = Math.round(data.feed_vol*100)/100;
    let feedingVolAdm = Math.round(data.feed_vol_adm*100)/100;
    let feedingData = feedingVol + feedingVolAdm
    return {
      feedingVol: feedingVol,
      feedingVolAdm: feedingVolAdm,
      feedingData: feedingData
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