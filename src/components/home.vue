<template>
  <div>This is the home page</div>
  <file-submit />
  <side-search />
</template>

<script>
import FileSubmit from "./fileSubmit.vue";
import SideSearch from "./sideSearch.vue";
export default {
  name: "home",
  components: { FileSubmit, SideSearch },
  props: {
    msg: String,
  },
  created() {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
