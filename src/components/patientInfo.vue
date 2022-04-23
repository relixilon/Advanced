<template>
  <div class="container" v-if="headers.length > 2">
    <card class="card" v-for="header in headers" :key="header">
      <h2>{{ header }}</h2>
      <p v-if="header === 'referral\r'">
        {{ prediction===1 ? 'Recommended': prediction===0 ? 'Not Recommended' : prediction===3 ? 'Not enough data':null}}

        </p>
      <p v-else>{{ patientData[header] }}</p>
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
  data: () => ({
  }),
  computed: {
    patientData() {
      return store.state.currentPatient;
    },
    prediction(){
      return store.state.currentPatientPrediction;
    },
    headers() {
      return Object.getOwnPropertyNames(store.state.currentPatient);
    },
  },
};
</script>
<style scoped>
@import '../assets/variables.css';

p {
  margin :0;
  padding-top: 3vh;
}

h2 { 
  margin: 0;
  padding: 0;
}

.container {
  display: flex;
  height: 85vh;
  flex-wrap: wrap;
}

.card {
  border: 1px solid;
  border-color: var(--tertiary-color);
  border-radius: 20px;
}
</style>
