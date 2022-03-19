<template>
  <div class="cardContainer">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {},
};
</script>

<style scoped>
.cardContainer {
  display: flex;
  flex-direction: column;
  width: 15vw;
  height: 15vh;
  padding: 10px;
  margin: 1vh;
  box-shadow: 0 10px 16px 0 rgba(0, 0, 0, 0.2);
}
</style>