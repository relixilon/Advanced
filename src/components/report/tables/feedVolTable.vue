<template>
  <table>
    <tr>
      <th>Feeding Vol</th>
      <th>Feeding Vol Administered</th>
    </tr>
    <tr>
      <td>{{ feedingVol }}</td>
      <td>{{ feedingVolAdm }}</td>
    </tr>
  </table>
</template>

<script>
import store from "@/store/index.js";

export default {
  name: 'FeedVolTable',
  data() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    let feedingVol = Math.round(data.feed_vol*100)/100;
    let feedingVolAdm = Math.round(data.feed_vol_adm*100)/100;
    return {
      feedingVol: feedingVol,
      feedingVolAdm: feedingVolAdm,
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
</style>