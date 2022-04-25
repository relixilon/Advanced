<template>
  <div class="header">
    <div class="logo">
      <img src="../assets/MOSA_Healthcare-logos_black.png" />
    </div>
    <div class="title">
      <h2>MOSA Dashboard</h2>
    </div>
    <router-link to="/">
      <button>Back</button>
    </router-link>
  </div>
  <div class="content">
    <form class="loginForm">
      <div>
        <h2>Username</h2>
        <input type="text" v-model="username" />
      </div>
      <div>
        <h2>Password</h2>
        <input type="password" v-model="password" />
      </div>
      <button type="button" v-on:click="submit()">Login</button>
      <span class="message">{{ msg }}</span>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import router from "../router/index";
import store from "../store/index";
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      msg: "",
    };
  },
  methods: {
    submit() {
      axios
        .post("http://127.0.0.1:5000/login", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          let res = response.data;
          if (res) {
            store.commit("setLoginState", true);
            store.commit("setUser", this.username);
            router.replace({ path: "/home" });
          } else {
            this.msg =
              "Incorrect Username or password. Please try again or contact an administrator";
          }
        });
    },
  },
};
</script>

<style scoped>
@import "../assets/variables.css";

.home-container {
  display: flex;
  overflow: hidden;
  background-color: var(--secondary-color);
}

.side-bar-container {
  display: flex;
  flex-direction: column;
  width: 12vw;
  height: 100vh;
  background-color: var(--primary-color);
}

img {
  height: 10vh;
  width: 20vw;
}
.header {
  display: flex;
  height: 10vh;
  flex-direction: row;
  border-bottom: 1px solid;
  background-color: var(--primary-color);
}

.logo {
  height: 10vh;
  width: 20vw;
  border-right: 1px solid;
}

.title {
  display: flex;
  align-items: center;
  height: 10vh;
  width: 100vw;
  background-color: var(--secondary-color);
}

.content {
  display: flex;
  width: 100%;
  height: 50vh;
  align-items: center;
  justify-content: center;
}

.loginForm {
  display: flex;
  flex-direction: column;
  height: 25vh;
  width: 10vw;
  justify-content: space-between;
}

.message {
  max-width: 20vw;
  color: red;
  font-style: italic;
}
</style>
