<template>
  <div>
    <!-- Health Records -->
    <md-content class="md-scrollbar">
      <div>
        <md-table v-model="logs" md-sort="timestamp" md-sort-order="desc" md-fixed-header>
          <md-table-row slot="md-table-row" slot-scope="{ item }">
            <md-table-cell md-label="Log Type" md-sort-by="type">{{ item.type }}</md-table-cell>
            <md-table-cell md-label="Value" md-sort-by="value">{{ item.value }}</md-table-cell>
            <md-table-cell md-label="Log Time" md-sort-by="timestamp">{{ item.timestamp }}</md-table-cell>
          </md-table-row>
        </md-table>
      </div>
    </md-content>
  </div>
</template>

<script>
export default {
  name: "health-log",
  data() {
    return {
      logs: []
    };
  },
  methods: {
    fetchData() {
      this.logs = [
        { type: "Blood Pressure", value: "100", timestamp: "2019/12/01 19:01" },
        { type: "Weight", value: "70kg", timestamp: "2019/12/01 19:01" },
        { type: "Blood Pressure", value: "100", timestamp: "2019/12/01 19:01" },
        { type: "Weight", value: "70kg", timestamp: "2019/12/01 19:01" },
        { type: "Blood Pressure", value: "100", timestamp: "2019/12/01 19:01" },
        { type: "Weight", value: "70kg", timestamp: "2019/12/01 19:01" },
        { type: "Blood Pressure", value: "100", timestamp: "2019/12/01 19:01" },
        { type: "Weight", value: "70kg", timestamp: "2019/12/01 19:01" }
      ];
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
