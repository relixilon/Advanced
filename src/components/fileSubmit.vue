   <template>
  <div class="container">
    <div>
      <h2>Load a file</h2>
      <hr />
      <label>File <input type="file" ref="doc" @change="readFile()" /> </label>
      <br />
      <button v-on:click="submitFile()">Submit</button>
    </div>
    {{ filecontent }}
  </div>
</template>
 
 
  <script>
export default {
  name: "pageMain",
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
      this.filecontent = this.content;
    },
  },
};
</script>
