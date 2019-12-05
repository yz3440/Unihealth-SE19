<template>
  <div id="app">
    <router-view name="header" />
    <fade-transition origin="center" mode="out-in" :duration="250">
      <router-view />
    </fade-transition>
  </div>
</template>

<script>
import { FadeTransition } from "vue2-transitions";
export default {
  name: "App",
  components: {
    FadeTransition
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
