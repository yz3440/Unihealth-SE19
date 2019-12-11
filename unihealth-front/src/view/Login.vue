<template>
  <div class="container">
    <form novalidate class="md-layout md-alignment-top-center" @submit.prevent="validateUser">
      <md-card class="md-layout-item md-size-50 md-small-size-100">
        <md-card-media-cover md-text-scrim>
          <md-card-media>
            <img :src="bgregister" alt="Landing" />
          </md-card-media>
          <md-card-area>
            <md-card-header>
              <div class="md-title">Login Unihealth</div>
            </md-card-header>
          </md-card-area>
        </md-card-media-cover>

        <md-card-content>
          <!-- Phone Number Field -->
          <md-field :class="getValidationClass('phone')">
            <label for="phone">Phone Number</label>
            <md-input
              type="phone"
              name="phone"
              id="phone"
              autocomplete="phone"
              v-model="form.phone"
              :disabled="sending"
            />
            <span class="md-error" v-if="!$v.form.phone.required">The phone number is required</span>
            <span class="md-error" v-else-if="!$v.form.phone.numeric">Invalid phone number</span>
          </md-field>

          <!-- Password Field -->
          <md-field :class="getValidationClass('password')">
            <label for="password">Password</label>
            <md-input
              type="password"
              name="password"
              id="password"
              autocomplete="password"
              v-model="form.password"
              :disabled="sending"
            />
            <span class="md-error" v-if="!$v.form.password.required">The password is required</span>
            <span class="md-error" v-else-if="!$v.form.password.minlength">The password is too short</span>
          </md-field>
        </md-card-content>

        <md-progress-bar md-mode="indeterminate" v-if="sending" />

        <md-card-actions>
          <md-button type="submit" class="md-primary" :disabled="sending">Login</md-button>
        </md-card-actions>
      </md-card>

      <md-snackbar :md-active.sync="userSaved">{{message}}</md-snackbar>
    </form>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";

import { required, minLength, numeric } from "vuelidate/lib/validators";

export default {
  name: "FormValidation",
  mixins: [validationMixin],
  props: {
    bgregister: {
      type: String,
      default: require("@/assets/img/bg-register.jpeg")
    }
  },
  data: () => ({
    form: {
      phone: null,
      password: null
    },
    userSaved: false,
    sending: false,
    message: null
  }),
  validations: {
    form: {
      phone: {
        required,
        numeric
      },
      password: {
        required,
        minLength: minLength(6)
      }
    }
  },
  methods: {
    getValidationClass(fieldName) {
      const field = this.$v.form[fieldName];

      if (field) {
        return {
          "md-invalid": field.$invalid && field.$dirty
        };
      }
    },
    clearForm() {
      this.$v.$reset();
      this.form.phone = null;
      this.form.password = null;
    },
    loginUser() {
      this.sending = true;

      // Pass in the Vue context
      // let that = this;

      console.log({
        phone: this.form.phone,
        password: this.form.password
      });

      // Pass in the Vue context
      let that = this;
      this.$http
        .post(
          "/auth/token",
          {
            phone: this.form.phone,
            password: this.form.password
          },
          { withCredentials: true }
        )
        .then(response => {
          console.log(response);
          that.message = response.data.msg;
          that.userSaved = true;
          that.sending = false;
          that.clearForm();
          that.$cookies.set("access_token", response.data.access_token);
          that.$cookies.set("refresh_token", response.data.refresh_token);
          that.$router.push("/profile");
        })
        .catch(error => {
          console.log(error);
          that.message = error.response.data.msg;
          that.userSaved = true;
          that.sending = false;
        });
    },
    validateUser() {
      this.$v.$touch();
      if (!this.$v.$invalid) {
        this.loginUser();
      }
    }
  },
  computed: {
    currentDate() {
      var today = new Date();
      var dd = today.getDate();
      var mm = today.getMonth() + 1; //Because January is 0
      var yyyy = today.getFullYear();

      if (dd < 10) dd = "0" + dd;
      if (mm < 10) mm = "0" + mm;

      today = yyyy + "-" + mm + "-" + dd;
      return today;
    }
  }
};
</script>

<style lang="scss" scoped>
.md-progress-bar {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
}
.container {
  margin-top: 100px;
}
</style>