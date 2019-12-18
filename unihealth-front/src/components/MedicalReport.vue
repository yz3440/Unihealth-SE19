<template>
  <div>
    <!-- Medical Reports -->
    <md-content class="md-scrollbar">
      <div>
        <md-table :value="reports" md-sort="created" md-sort-order="desc" md-fixed-header>
          <md-table-row slot="md-table-row" slot-scope="{ item }">
            <md-table-cell md-label="Related Disease" md-sort-by="disease">{{ item.disease }}</md-table-cell>
            <!-- <md-table-cell md-label="Medication" md-sort-by="medication">{{ item.medication }}</md-table-cell> -->
            <md-table-cell md-label="Medical Note" md-sort-by="note">{{ item.note }}</md-table-cell>
            <md-table-cell md-label="Report Time" md-sort-by="-created">{{ item.created }}</md-table-cell>
          </md-table-row>
        </md-table>
      </div>
    </md-content>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "medical-report",
  computed: {
    ...mapGetters({
      reports: "medicalReports"
    })
  },
  methods: {
    fetchData() {
      this.$store.dispatch("fetchMedicalReports");
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
