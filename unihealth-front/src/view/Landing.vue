<template>
  <div class="container">
    <div class="md-layout md-alignment-top-center">
      <div class="md-layout-item md-size-50 md-xsmall-size-100">
        <md-card md-with-hover>
          <md-card-media-cover md-text-scrim>
            <md-card-media md-ratio="16:9">
              <img :src="bglanding" alt="Landing" />
            </md-card-media>

            <md-card-area>
              <md-card-header>
                <h1 class="md-title">Unihealth</h1>
                <h2 class="md-subhead">Your Health Records, Unified</h2>
              </md-card-header>

              <md-card-content class="md-size-80">
                Unihealth helps the patient to view past diagnosis from different hospitals,
                add daily health logs for later references,
                and also receive notifications for regular medications.
              </md-card-content>
              <md-card-actions md-alignment="right">
                <md-button href="#/login" class="md-primary md-lg">Login</md-button>
                <md-button href="#/register" class="md-primary md-lg">Register Now</md-button>
              </md-card-actions>
            </md-card-area>
          </md-card-media-cover>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Landing",
  data() {
    return {
      msg: "Welcome to Unihealth"
    };
  },
  props: {
    bglanding: {
      type: String,
      default: require("@/assets/img/bg-landing.jpg")
    }
  }
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
