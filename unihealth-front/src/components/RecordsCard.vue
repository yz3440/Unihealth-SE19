<template>
  <div>
    <!-- Health Records -->
    <md-tabs md-sync-route class="md-transparent">
      <md-tab id="tab-health-log" md-label="Health Log" to="/profile" exact>
        <health-log></health-log>
      </md-tab>
      <md-tab id="tab-medical-report" md-label="Medical Report" to="/profile/report">
        <medical-report></medical-report>
      </md-tab>
      <md-tab id="tab-medical-reminder" md-label="Medication Reminder" to="/profile/medication">
        <medication-reminder></medication-reminder>
      </md-tab>
    </md-tabs>
  </div>
</template>

<script>
import HealthLog from "../components/HealthLog";
import MedicalReport from "../components/MedicalReport";
import MedicationReminder from "../components/MedicationReminder";

export default {
  name: "records-card",
  components: { HealthLog, MedicalReport, MedicationReminder },
  data() {
    return {};
  },
  methods: {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.md-tab {
  padding: 0px;
  margin-top: 10px;
}
</style>
