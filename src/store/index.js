import Vuex from 'vuex'
// eslint-disable-next-line no-unused-vars
import axios from 'axios';
export default new Vuex.Store({
  state: { // = Data
    patients: [],
    currentPatient: [],
    currentPatientPrediction: 0
  },
  getters: {
    patientCount() { // = computed
      //.....
    },
  },
  actions: {
      predict({commit}, patient){
        axios
        .post("http://127.0.0.1:5000/predict", {
          encounterId:patient.encounterId,
          end_tidal_co2:patient.end_tidal_co2,
          feed_vol:patient.feed_vol,
          feed_vol_adm:patient.feed_vol_adm,
          fio2:patient.fio2,
          fio2_ratio:patient.fio2_ratio,
          insp_time:patient.insp_time,
          oxygen_flow_rate:patient.oxygen_flow_rate,
          peep:patient.peep,
          pip:patient.pip,
          resp_rate:patient.resp_rate,
          sip:patient.sip,
          tidal_vol:patient.tidal_vol,
          tidal_vol_actual:patient.tidal_vol_actual,
          tidal_vol_kg:patient.tidal_vol_kg,
          tidal_vol_spon:patient.tidal_vol_spon,
          bmi:patient.bmi,
        })
        .then((response) => {
          //console.log(response);
          let prediction = response.data;
          commit('setPatientReferral',prediction)
        }); 
      }
  },
  mutations: {
    setPatients(state, patients) {
      state.patients = patients
    },
    setCurrentPatient(state, data) {
      state.currentPatient = data
    },
    setPatientReferral(state,referral){
      state.currentPatientPrediction = referral
    }

  }
})
