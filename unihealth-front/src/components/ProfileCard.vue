<template>
  <div>
    <!-- Profile Card -->
    <md-card class="md-transparent">
      <md-card-header>
        <div class="md-title">{{profile.firstName}} {{profile.lastName}}</div>
        <div class="md-subhead">{{profile.role?profile.role.toUpperCase():null}}</div>
      </md-card-header>
      <md-card-content>
        <span>Phone: {{profile.phone}}</span>
        <br />
        <span>Gender: {{profile.gender}}</span>
        <br />
        <span>Birthday: {{profile.birthday}}</span>
      </md-card-content>
    </md-card>
    <br />

    <!-- Guest Profile Card -->
    <md-card v-if="guestProfile.phone" class="md-transparent">
      <md-card-header>
        <div class="md-title">{{guestProfile.firstName}} {{guestProfile.lastName}}</div>
        <div class="md-subhead">GUEST PATIENT</div>
      </md-card-header>

      <md-card-content>
        <span>Phone: {{guestProfile.phone}}</span>
        <br />
        <span>Gender: {{guestProfile.gender}}</span>
        <br />
        <span>Birthday: {{guestProfile.birthday}}</span>
      </md-card-content>
    </md-card>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "profile-card",
  computed: {
    ...mapGetters({
      profile: "userProfile",
      guestProfile: "guestProfile"
    })
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
