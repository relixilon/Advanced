<template>
  <bar />
  <home msg="Welcome to Your Vue.js App" />
</template>

<script>
import home from "./components/home.vue";
import bar from "./components/bar.vue";

export default {
  name: "App",
  components: {
    home,
    bar,
  },
};
</script>

<style>
</style>
