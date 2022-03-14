<template>
  <input type="text" v-model="name" />
  {{ name }}
</template>

<script>
export default {
  name: "test",
  data() {
    return {
      name: "Mario",
    };
  },
  methods: {
    textChange(event) {
      this.name = event.value;
    },
  },
};
</script>

<style>
</style>