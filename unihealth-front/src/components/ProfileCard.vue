<template>
  <div>
    <!-- Profile Card -->
    <md-card class="md-transparent">
      <md-card-header>
        <div class="md-title">{{profile.firstName}} {{profile.lastName}}</div>
        <div class="md-subhead">Tel: {{profile.phone}}</div>
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
        <md-list-item @click="openLogDialog">Log Your Health</md-list-item>
      </md-list>
    </md-card>

    <md-dialog :md-active.sync="dialogOpened">
      <md-dialog-title>Log Your Health</md-dialog-title>

      <md-tabs md-dynamic-height>
        <md-tab md-label="Add Quick Health Log">
          <div class="md-layout md-gutter">
            <!-- Type Field -->
            <div class="md-layout-item">
              <md-field>
                <label for="type">Log Type</label>
                <md-select
                  name="healthLogType"
                  id="healthLogType"
                  v-model="healthLogForm.type"
                  md-dense
                  :disabled="sending"
                >
                  <md-option value="Blood Pressure (mmHg)">Blood Pressure (mmHg)</md-option>
                  <md-option value="Weight (kg)">Weight (kg)</md-option>
                </md-select>
              </md-field>
            </div>

            <!-- Value Field -->
            <div class="md-layout-item">
              <md-field>
                <label for="value">Value</label>
                <md-input v-model="healthLogForm.value" />
              </md-field>
            </div>
          </div>
        </md-tab>
      </md-tabs>

      <md-dialog-actions>
        <md-button class="md-primary" @click="dialogOpened = false">Close</md-button>
        <md-button @click="addQuickLog" class="md-primary" :disabled="sending">Add</md-button>
      </md-dialog-actions>
    </md-dialog>
    <md-snackbar :md-active.sync="logSaved">{{message}}</md-snackbar>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";

import { required, numeric } from "vuelidate/lib/validators";
export default {
  name: "profile-card",
  data() {
    return {
      profile: {
        firstName: null,
        lastName: null,
        gender: null,
        birthday: null,
        phone: null
      },
      healthLogForm: {
        type: null,
        value: null
      },
      dialogOpened: false,
      sending: false,
      logSaved: false,
      message: null
    };
  },
  validations: {
    type: {
      required
    },
    value: {
      required,
      numeric
    }
  },
  methods: {
    fetchData() {
      let that = this;
      this.$http
        .get("/resources/user", {
          headers: {
            Authorization: "Bearer " + this.$cookies.get("access_token")
          }
        })
        .then(response => {
          that.profile = {
            firstName: response.data.first_name,
            lastName: response.data.last_name,
            gender: response.data.gender,
            birthday: response.data.birthday,
            phone: response.data.phone
          };
        })
        .catch(error => {
          console.log(error);
        });
    },
    openLogDialog() {
      this.dialogOpened = true;
    },
    addQuickLog() {
      console.log(this.healthLogForm);
      this.sending = true;
      // Pass in the Vue context
      let that = this;
      this.$http
        .post(
          "/resources/health_logs",
          {
            type: this.healthLogForm.type,
            value: this.healthLogForm.value
          },
          {
            headers: {
              Authorization: "Bearer " + this.$cookies.get("access_token")
            }
          }
        )
        .then(response => {
          console.log(response);
          that.message = response.data.msg;
          that.logSaved = true;
          that.sending = false;
          that.dialogOpened = false;
          that.clearForm();
        })
        .catch(error => {
          console.log(error);
          that.message = error.response.data.msg;
          that.logSaved = true;
          that.sending = false;
        });
    },
    clearForm() {
      this.healthLogForm.type = null;
      this.healthLogForm.value = null;
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
</style>
