   <template>
  <div class="container">
    <div class="fileInput">
      <button class="submitFile">
        <label>
          Upload File
          <input
            type="file"
            class="hide"
            ref="doc"
            accept=".csv"
            @change="readFile()"
          />
        </label>
      </button>
      <br />
      <button class="submitFile" type="submit" v-on:click="submitFile()">
        Submit
      </button>
    </div>
  </div>
</template>
 
<script>
import store from "@/store/index.js";
import csvJSON from "@/functions/csvJSON";
export default {
  components: {},
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
<style scoped>
.container {
  display: flex;
  width: 100%;
  height: 10vh;
}

.fileInput {
  display: flex;
  flex-direction: column;
  width: 12vw;
}

.submitFile {
  background-color: lightblue;
  height: 10vh;
}

.hide {
  opacity: 0;
  width: 0;
  height: 0;
}
</style>
