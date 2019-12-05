<template>
  <div>
    <!-- Health Records -->

    <md-content class="md-scrollbar">
      <md-list>
        <md-list-item v-for="log in logs" v-bind:key="log.message">
          <div class="md-layout md-gutter">
            <div class="md-layout-item">{{log.type}}</div>
            <div class="md-layout-item">{{log.value}}</div>
            <div class="md-layout-item">{{log.timestamp}}</div>
          </div>
        </md-list-item>
      </md-list>
    </md-content>
  </div>
</template>

<script>
export default {
  name: "health-log",
  data() {
    return {
      logs: [
        { type: "Blood Pressure", value: "100", timestamp: "2019/12/01 19:01" },
        { type: "Weight", value: "70kg", timestamp: "2019/12/01 19:01" }
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
  max-height: 500px;
  overflow: auto;
}
</style>
