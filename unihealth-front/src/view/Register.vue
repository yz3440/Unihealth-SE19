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
              <div class="md-title">Join Unihealth as a Patient User</div>
            </md-card-header>
          </md-card-area>
        </md-card-media-cover>

        <md-card-content>
          <div class="md-layout md-gutter">
            <!-- First Name Field -->
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('firstName')">
                <label for="first-name">First Name</label>
                <md-input
                  name="first-name"
                  id="first-name"
                  autocomplete="given-name"
                  v-model="form.firstName"
                  :disabled="sending"
                />
                <span class="md-error" v-if="!$v.form.firstName.required">The first name is required</span>
                <span class="md-error" v-else-if="!$v.form.firstName.minlength">Invalid first name</span>
              </md-field>
            </div>

            <!-- Last Name Field -->
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('lastName')">
                <label for="last-name">Last Name</label>
                <md-input
                  name="last-name"
                  id="last-name"
                  autocomplete="family-name"
                  v-model="form.lastName"
                  :disabled="sending"
                />
                <span class="md-error" v-if="!$v.form.lastName.required">The last name is required</span>
                <span class="md-error" v-else-if="!$v.form.lastName.minlength">Invalid last name</span>
              </md-field>
            </div>
          </div>

          <!-- Gender Field -->
          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('gender')">
                <label for="gender">Gender</label>
                <md-select
                  name="gender"
                  id="gender"
                  v-model="form.gender"
                  md-dense
                  :disabled="sending"
                >
                  <md-option value="Male">Male</md-option>
                  <md-option value="Female">Female</md-option>
                </md-select>
                <span class="md-error">The gender is required</span>
              </md-field>
            </div>

            <!-- Birthday Field -->
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('birthday')">
                <label for="date">Birthday</label>
                <md-input
                  type="date"
                  id="birthday"
                  name="birthday"
                  autocomplete="birthday"
                  v-model="form.birthday"
                  :max="currentDate"
                  placeholder=" "
                  :disabled="sending"
                />
                <span class="md-error" v-if="!$v.form.birthday.required">The birthday is required</span>
              </md-field>
            </div>
          </div>

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
          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
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
                <span
                  class="md-error"
                  v-else-if="!$v.form.password.minlength"
                >The password is too short</span>
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('repeatPassword')">
                <label for="repeatPassword">Repeat Password</label>
                <md-input
                  type="password"
                  id="repeatPassword"
                  name="repeatPassword"
                  autocomplete="repeatPassword"
                  v-model="form.repeatPassword"
                  :disabled="sending"
                />
                <span
                  class="md-error"
                  v-if="!$v.form.repeatPassword.required"
                >The repeated password is required</span>
                <span
                  class="md-error"
                  v-else-if="!$v.form.repeatPassword.sameAsPassword"
                >The password does not match</span>
              </md-field>
            </div>
          </div>
        </md-card-content>

        <md-progress-bar md-mode="indeterminate" v-if="sending" />

        <md-card-actions>
          <md-button href="#/register" class="md-accent">I'm a Doctor</md-button>
          <md-button type="submit" class="md-primary" :disabled="sending">Create new patient user</md-button>
        </md-card-actions>
      </md-card>

      <md-snackbar :md-active.sync="userSaved">{{message}}</md-snackbar>
    </form>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";

import {
  required,
  minLength,
  maxLength,
  numeric,
  sameAs
} from "vuelidate/lib/validators";

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
      firstName: null,
      lastName: null,
      gender: null,
      birthday: null,
      phone: null,
      password: null,
      repeatPassword: null
    },
    userSaved: false,
    sending: false,
    message: null
  }),
  validations: {
    form: {
      firstName: {
        required,
        minLength: minLength(3)
      },
      lastName: {
        required,
        minLength: minLength(3)
      },
      birthday: {
        required
      },
      gender: {
        required
      },
      phone: {
        required,
        numeric
      },
      password: {
        required,
        minLength: minLength(6)
      },
      repeatPassword: {
        required,
        sameAsPassword: sameAs("password")
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
      this.form.firstName = null;
      this.form.lastName = null;
      this.form.gender = null;
      this.form.birthday = null;
      this.form.phone = null;
      this.form.password = null;
      this.form.repeatPassword = null;
    },
    saveUser() {
      this.sending = true;

      // Pass in the Vue context
      let that = this;
      this.$http
        .post("/resources/user", {
          firstName: this.form.firstName,
          lastName: this.form.lastName,
          gender: this.form.gender,
          birthday: this.form.birthday,
          phone: this.form.phone,
          password: this.form.password
        })
        .then(response => {
          console.log(response);
          that.message = response.data.msg;
          that.userSaved = true;
          that.sending = false;
          that.clearForm();
          that.$router.push("/login");
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
        this.saveUser();
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