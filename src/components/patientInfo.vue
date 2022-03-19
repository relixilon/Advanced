<template>
  <div class="container" v-if="headers.length > 2">
    <card class="card" v-for="header in headers" :key="header">
      <h2>{{ header }}</h2>
      <p>{{ patientData[header] }}</p>
    </card>
  </div>
</template>

<script>
import card from "@/components/card.vue";
import store from "@/store/index.js";
export default {
  components: {
    card,
  },
  computed: {
    patientData() {
      return store.state.currentPatient;
    },
    headers() {
      return Object.getOwnPropertyNames(store.state.currentPatient);
    },
  },
};
</script>
<style scoped>
.container {
  display: flex;
  height: 90vh;
  flex-wrap: wrap;
}
</style>