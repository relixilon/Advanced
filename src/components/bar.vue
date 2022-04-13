<template>
  <div class="bar">
    <ul>
      <li><button v-on:click="changeComp('patient-info')">Overview</button></li>
      <li><button v-on:click="changeComp('charts')">Charts</button></li>
      <li>
        <button>
          <router-link to="/report">Generate report</router-link>
        </button>
      </li>
    </ul>
    <ul class="login">
      <li>Login</li>
      <li>Register</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "bar",
  methods: {
    changeComp (component) {
      this.$emit("changeComp", component)
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.bar {
  display: flex;
  width: 100vw;
  background-color: black;
  color: white;
  height: 4vh;
  align-items: center;
  justify-content: space-between;
}

ul {
  display: flex;
  flex-direction: row;
  list-style: none;
}
li {
  margin: 0 2vw 0 0;
}

li:hover {
  font-size: 20px;
}

.login {
  order: 1;
}

</style>
