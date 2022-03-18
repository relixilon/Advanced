<template>
  <div>
    <h2>{{ title }}</h2>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    title: String,
  },
};
</script>

<style>
</style>