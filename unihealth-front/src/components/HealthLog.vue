<template>
  <div>
    <!-- Health Records -->
    <md-content class="md-scrollbar">
      <div>
        <md-table v-model="logs" md-sort="timestamp" md-sort-order="desc" md-fixed-header>
          <md-table-row slot="md-table-row" slot-scope="{ item }">
            <md-table-cell md-label="Log Type" md-sort-by="type">{{ item.log_type }}</md-table-cell>
            <md-table-cell md-label="Value" md-sort-by="value">{{ item.log_value }}</md-table-cell>
            <md-table-cell md-label="Log Time" md-sort-by="timestamp">{{ item.created }}</md-table-cell>
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
      let that = this;
      this.$http
        .get("/resources/health_logs", {
          headers: {
            Authorization: "Bearer " + this.$cookies.get("access_token")
          }
        })
        .then(response => {
          console.log(response);
          that.logs = response.data;
        })
        .catch(error => {
          console.log(error);
        });
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
