<template>
  <div>
    <!-- Health Records -->
    <md-tabs md-sync-route class="md-transparent">
      <md-tab id="tab-health-log" md-label="Health Log" to="/profile" exact>
        <health-log></health-log>
      </md-tab>
      <md-tab id="tab-medical-report" md-label="Medical Report" to="/profile/report">
        <md-list>
          <md-list-item to="/components/tabs/pages/1">Go to Subpage 1</md-list-item>
          <md-list-item to="/components/tabs/pages/2">Go to Subpage 2</md-list-item>
        </md-list>
      </md-tab>
      <md-tab id="tab-medical-reminder" md-label="Medication Reminder" to="/profile/medication">
        <md-list>
          <md-list-item to="/components/tabs/pages/1">Go to Subpage 1</md-list-item>
          <md-list-item to="/components/tabs/pages/2">Go to Subpage 2</md-list-item>
        </md-list>
      </md-tab>
    </md-tabs>
  </div>
</template>

<script>
import HealthLog from "../components/HealthLog";

export default {
  name: "records-card",
  components: { HealthLog },
  data() {
    return {
      profile: {}
    };
  },
  props: {
    bglanding: {
      type: String,
      default: require("@/assets/img/bg-landing.jpg")
    }
  },
  methods: {
    addQuickLog() {
      alert("dfs");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.md-tab {
  padding: 0px;
  margin-top: 10px;
}
</style>
