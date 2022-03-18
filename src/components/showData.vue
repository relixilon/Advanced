t <template>
  <table v-if="json">
    <tr>
      <th>encounterId</th>
      <th>End Tidal CO2</th>
      <th>Feed vol</th>
      <th>Feed vol adm</th>
      <th>Fio2</th>
      <th>Insp time</th>
      <th>Oxygen Flow Rate</th>
      <th>Peep</th>
      <th>Pip</th>
      <th>Resp Rate</th>
      <th>Sip</th>
      <th>Tidal vol</th>
      <th>Tidal vol actual</th>
      <th>Tidal vol kg</th>
      <th>Tidal vol spon</th>
      <th>BMI</th>
      <th>Referral</th>
    </tr>
    <tr v-for="item in patients" :key="item.encounterId">
      <td>{{ item.encounterId }}</td>
      <td>{{ item.end_tidal_co2 }}</td>
      <td>{{ item.feed_vol }}</td>
      <td>{{ item.feed_vol_adm }}</td>
      <td>{{ item.fio2 }}</td>
      <td>{{ item.insp_time }}</td>
      <td>{{ item.oxygen_flow_rate }}</td>
      <td>{{ item.peep }}</td>
      <td>{{ item.pip }}</td>
      <td>{{ item.resp_rate }}</td>
      <td>{{ item.sip }}</td>
      <td>{{ item.tidal_vol }}</td>
      <td>{{ item.tidal_vol_actual }}</td>
      <td>{{ item.tidal_vol_kg }}</td>
      <td>{{ item.tidal_vol_spon }}</td>
      <td>{{ item.bmi }}</td>
      <td>{{ item.referral }}</td>
    </tr>
  </table>
</template>

<script>
import store from "@/store/index.js";
//import VueJsonPretty from "vue-json-pretty";
import "vue-json-pretty/lib/styles.css";
export default {
  name: "showData",
  props: {
    json: JSON,
  },
  components: {
    //  VueJsonPretty,
  },
  computed: {
    patients() {
      return store.state.patients;
    },
  },
};
</script>

<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td,
th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}

.content {
  height: 70vh;
  overflow: scroll;
}
</style>