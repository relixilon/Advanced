<template>
  <ul>
    <li v-for="item in JSON.parse(json)" :key="item.encounterId">
      {{ item }}
    </li>
  </ul>
</template>

<script>
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
};
</script>

<style>
</style>