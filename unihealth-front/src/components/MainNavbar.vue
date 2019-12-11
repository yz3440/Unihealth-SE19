<template>
  <md-toolbar class="md-transparent" md-elevation="1">
    <!-- <h3 class="md-title" style="flex: 1">Unihealth</h3> -->
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
    logoutUser() {}
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