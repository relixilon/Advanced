<template>
  <div>This is the home page</div>
  <file-submit />
</template>

<script>
import FileSubmit from "./fileSubmit.vue";
export default {
  name: "home",
  components: { FileSubmit },
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  height: 2vh;
}
</style>
