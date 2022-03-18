   <template>
  <div class="container">
    <div>
      <h2>Load a file</h2>
      <hr />
      <label>File <input type="file" ref="doc" @change="readFile()" /> </label>
      <br />
      <button v-on:click="submitFile()">Submit</button>
    </div>
    <show-data :json="Hello" />
  </div>
</template>
 
<script>
import store from "@/store/index.js";
import csvJSON from "@/functions/csvJSON";
import showData from "./showData.vue";
export default {
  components: { showData },
  name: "FileSubmit",
  props: {
    msg: String,
  },
  data() {
    return {
      filecontent: "",
    };
  },

  methods: {
    readFile() {
      this.file = this.$refs.doc.files[0];
      const reader = new FileReader();
      reader.onload = (res) => {
        this.content = res.target.result;
      };
      reader.onerror = (err) => console.log(err);
      reader.readAsText(this.file);
    },
    submitFile() {
      this.filecontent = JSON.parse(csvJSON(this.content));
      store.commit("setPatients", this.filecontent);
    },
  },
};
</script>
