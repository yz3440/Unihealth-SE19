<template>
  <div>
    <!-- Medication Reminder -->
    <md-content class="md-scrollbar">
      <div>
        <md-table v-model="reports" md-sort="timestamp" md-sort-order="asc" md-fixed-header>
          <md-table-row slot="md-table-row" slot-scope="{ item }">
            <md-table-cell md-label="Medication" md-sort-by="medication">{{ item.medication }}</md-table-cell>
            <md-table-cell md-label="Disease" md-sort-by="disease">{{ item.disease }}</md-table-cell>
            <md-table-cell
              md-label="Next Time of Intake"
              md-sort-by="timestamp"
            >{{ item.timestamp }}</md-table-cell>
          </md-table-row>
        </md-table>
      </div>
    </md-content>
  </div>
</template>

<script>
export default {
  name: "medication-reminder",
  data() {
    return {
      reports: [
        {
          disease: "Diabetes",
          medication: "Insulin shots",
          timestamp: "2019/12/08 19:00"
        },
        {
          disease: "Diabetes",
          medication: "Insulin shots",
          timestamp: "2019/12/09 19:00"
        },
        {
          disease: "Diabetes",
          medication: "Insulin shots",
          timestamp: "2019/12/10 19:01"
        }
      ]
    };
  },
  methods: {}
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
