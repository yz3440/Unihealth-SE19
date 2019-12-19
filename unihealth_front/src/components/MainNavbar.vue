<template>
  <md-toolbar class="md-transparent" md-elevation="1">
    <a href="#/" class="md-title">Unihealth</a>
    <span style="flex: 1"></span>
    <md-button href="#/login" class="md-primary" v-if="showLogin">Login</md-button>
    <md-button href="#/register" class="md-primary" v-if="showLogin">Register</md-button>
    <md-button @click="logoutUser" class="md-primary" v-else>Logout</md-button>
  </md-toolbar>
</template>

<script>
export default {
  name: "MainNavbar",
  methods: {
    logoutUser() {
      let that = this;
      this.$http
        .delete("/auth/token", {
          headers: {
            Authorization: "Bearer " + localStorage.access_token
          },
          data: {
            refresh_token: localStorage.refresh_token
          }
        })
        .then(response => {
          console.log(response);
          localStorage.access_token = null;
          localStorage.refresh_token = null;
          that.$store.commit("resetState");
          that.$router.push("/");
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  computed: {
    showLogin() {
      const excludedRoutes = ["/profile"];
      return excludedRoutes.every(res => {
        return !this.$route.path.startsWith(res);
      });
    }
  }
};
</script>

<style>
.md-title {
  text-align: left;
}
a {
  text-decoration: none !important;
}
</style>