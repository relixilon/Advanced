<template>
<div class="chart-info">
  <h1>Patient Report #{{ encounterId }}</h1>
</div>
</template>

<script>
import store from "@/store/index.js";

export default {
  name: 'ChartInfo',
  data() {
    const data = JSON.parse(JSON.stringify(store.state.currentPatient));
    return {
      encounterId: data.encounterId,
    }
  }
}</script>