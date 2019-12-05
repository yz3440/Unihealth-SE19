<template>
  <div>
    <!-- Profile Card -->
    <md-card class="md-transparent">
      <md-card-header>
        <div class="md-title">{{profile.firstName}} {{profile.lastName}}</div>
        <div class="md-subhead">{{profile.email}}</div>
      </md-card-header>

      <md-card-content>
        <span>Gender: {{profile.gender}}</span>
        <br />
        <span>Birthday: {{profile.birthday}}</span>
      </md-card-content>

      <md-card-actions>
        <md-button class="md-primary">Edit</md-button>
      </md-card-actions>
    </md-card>

    <!-- Action List -->
    <md-card class="md-transparent" style="margin-top:10px">
      <md-list>
        <md-list-item @click="addQuickLog">Add Quick Health Log</md-list-item>
      </md-list>
    </md-card>
  </div>
</template>

<script>
export default {
  name: "profile-card",
  data() {
    return {
      profile: {
        firstName: null,
        lastName: null,
        gender: null,
        birthday: null,
        email: null
      }
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
      alert("Adding quick log");
    },
    updateProfileData() {
      this.profile = {
        firstName: "Yufeng",
        lastName: "Zhao",
        gender: "Male",
        birthday: "1998-06-08",
        email: "yz3440@nyu.edu"
      };
    }
  },
  mounted() {
    this.updateProfileData();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
</style>
