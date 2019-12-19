<template>
  <div>
    <!-- Health Records -->
    <md-content class="md-scrollbar">
      <div>
        <md-table :value="logs" md-sort="created" md-sort-order="desc" md-fixed-header>
          <md-table-row slot="md-table-row" slot-scope="{ item }">
            <md-table-cell md-label="Log Type" md-sort-by="log_type">{{ item.log_type }}</md-table-cell>
            <md-table-cell md-label="Value" md-sort-by="log_value">{{ item.log_value }}</md-table-cell>
            <md-table-cell md-label="Log Time" md-sort-by="-created">{{ item.created }}</md-table-cell>
          </md-table-row>
        </md-table>
      </div>
    </md-content>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "health-log",
  computed: {
    ...mapGetters({
      logs: "healthLogs"
    })
  },
  methods: {
    fetchData() {
      this.$store.dispatch("fetchHealthLogs");
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
