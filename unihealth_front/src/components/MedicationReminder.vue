<template>
  <div>
    <!-- Medication Reminder -->
    <md-content class="md-scrollbar">
      <div>
        <md-table :value="reminders" md-sort="created" md-sort-order="desc" md-fixed-header>
          <md-table-row slot="md-table-row" slot-scope="{ item }">
            <md-table-cell md-label="Medicine" md-sort-by="medicine">{{ item.medicine }}</md-table-cell>
            <md-table-cell md-label="Amount" md-sort-by="amount">{{ item.amount }}</md-table-cell>
            <md-table-cell md-label="Disease" md-sort-by="disease">{{ item.disease }}</md-table-cell>
            <md-table-cell md-label="Next Time of Intake" md-sort-by="created">{{ item.created }}</md-table-cell>
          </md-table-row>
        </md-table>
      </div>
    </md-content>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "medication-reminder",
  computed: {
    ...mapGetters({
      reminders: "medicationReminders"
    })
  },
  methods: {
    fetchData() {
      this.$store.dispatch("fetchMedicationReminders");
    }
  },
  mounted() {
    this.fetchData();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
.md-content {
  height: 500px;
  max-height: 500px;
  overflow: auto;
}
</style>
