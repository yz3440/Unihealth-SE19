<template>
  <div class="container">
    <div class="md-layout md-alignment-top-center md-gutter">
      <!-- Left section -->
      <div class="md-layout-item md-size-20">
        <!-- Profile Card -->
        <profile-card></profile-card>
        <!-- Action Card -->
        <action-card></action-card>
      </div>

      <!-- Right section -->
      <div class="md-layout-item md-size-50 md-xsmall-size-100">
        <!-- Health Record -->
        <records-card></records-card>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileCard from "../components/ProfileCard";
import RecordsCard from "../components/RecordsCard";
import ActionCard from "../components/ActionCard";

export default {
  name: "profile",
  components: {
    ProfileCard,
    RecordsCard,
    ActionCard
  },
  data() {
    return {};
  },
  mounted() {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

.container {
  margin-top: 100px;
}
</style>
