<template>
<body>
  <div class="header">
    <div class="logo">
      <img src="../assets/MOSA_Healthcare-logos_black.png" />
    </div>
    
    
  </div>
  
   
    <form >
      <div class="loginForm">
        <label for="username"><b>Username :</b></label>
        <br><br>
        <input type="text" placeholder="Enter username" v-model="username"/>
        <br><br>
        <label for="psw"><b>Password :</b></label>
        <br><br>
        <input type="password" placeholder="Enter password" v-model="password" />
        <br><br>
        <button type="button" v-on:click="submit()">Login</button>
      <span class="message">{{ msg }}</span>
      </div>
    </form>
   
</body>
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

img {
  height: 10vh;
  width: 30vw;
}
.header {
  display: flex;
  height: 10vh;
  flex-direction: row;
  border-bottom: 10px outset;
  /* border-color: #19aec9;  */
  box-shadow: 7px 7px rgb(66, 66, 66);
  background-color: var(--primary-color);
}


.logo {
  height: 10vh;
  width: 60vw;
  /* border-right: 10px solid; */
}

.loginForm {
  
  padding: 40px;
  text-align: center;
  background-color: whitesmoke;
}

.message {
  max-width: 20vw;
  color: red;
  font-style: italic;
}
form {border: 6px outset #19aec9;
      margin: 100px;
      box-shadow: 7px 7px rgb(83, 83, 83);
      margin-top: 100px;
      margin-left:  350px;
      margin-right: 250px;
      
      }
input[type=text], input[type=password] {
  width: 40%;
  padding: 12px 20px;
  margin: 10px 0;
  margin-left: 180px;
  margin-right: 250px;
  display: inline-block;
  border: 3px solid #19aec9;
  background-color: #ffffff;
}

button {
  background-color: #19aec9;
  color: black;
  padding: 10px 14px;
  margin: 20px 0;
  margin-left: 230px;
  margin-right: 250px;
  cursor: pointer;
  width: 30%;
  text-align: center;
  border: 3px solid #9c9c9c;
}

button:hover {
  opacity: 0.6;
}
body{
  background-color: rgb(201, 199, 199);
  height: 752px;
  
}
</style>
