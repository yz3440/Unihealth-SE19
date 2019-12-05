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

        <!-- First Name Field -->
        <md-card-content>
          <div class="md-layout md-gutter">
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

          <!-- Email Field -->
          <md-field :class="getValidationClass('email')">
            <label for="email">Email</label>
            <md-input
              type="email"
              name="email"
              id="email"
              autocomplete="email"
              v-model="form.email"
              :disabled="sending"
            />
            <span class="md-error" v-if="!$v.form.email.required">The email is required</span>
            <span class="md-error" v-else-if="!$v.form.email.email">Invalid email</span>
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

      <md-snackbar :md-active.sync="userSaved">The user {{ lastUser }} was saved with success!</md-snackbar>
    </form>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import {
  required,
  email,
  minLength,
  maxLength,
  maxValue,
  sameAs
} from "vuelidate/lib/validators";

export default {
  name: "register-card",
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
      age: null,
      birthday: null,
      email: null,
      password: null,
      repeatPassword: null
    },
    userSaved: false,
    sending: false,
    lastUser: null
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
      age: {
        required,
        maxLength: maxLength(3)
      },
      gender: {
        required
      },
      email: {
        required,
        email
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
      this.form.birthday = null;
      this.form.age = null;
      this.form.gender = null;
      this.form.email = null;
      this.form.password = null;
      this.form.repeatPassword = null;
    },
    saveUser() {
      this.sending = true;

      // Instead of this timeout, here you can call your API
      window.setTimeout(() => {
        this.lastUser = `${this.form.firstName} ${this.form.lastName}`;
        this.userSaved = true;
        this.sending = false;
        this.clearForm();
      }, 1500);
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
</style>