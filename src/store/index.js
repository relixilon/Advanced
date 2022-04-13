import Vuex from 'vuex'

export default new Vuex.Store({
  state: { // = Data
    patients: [],
    currentPatient: [],
  },
  getters: {
    patientCount() { // = computed
      //.....
    },
  },
  actions: {
    fetchPatients() { // = methods
      //...
    }
  },
  mutations: {
    setPatients(state, patients) {
      state.patients = patients
    },
    setCurrentPatient(state, data) {
      state.currentPatient = data
    },

  }
})
