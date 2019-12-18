<template>
  <div>
    <!-- Action List -->
    <!-- Doctor-Only Action of Setting Guest Patient -->
    <div v-if="profile.role=='doctor'">
      <md-card class="md-transparent" style="margin-top:10px">
        <md-list>
          <md-list-item @click="openSetGuestDialog">Set Your Guest Patient</md-list-item>
        </md-list>
      </md-card>

      <md-dialog-prompt
        :md-active.sync="setGuestDialogOpened"
        v-model="patientPhone"
        md-title="Who is your patient now?"
        md-input-placeholder="Type his/her phone number..."
        md-confirm-text="Done"
      />
    </div>

    <div v-if="profile.role == 'patient' || guestProfile.phone">
      <md-card class="md-transparent" style="margin-top:10px">
        <md-list>
          <md-list-item @click="openLogDialog">Add Health Record</md-list-item>
        </md-list>
      </md-card>

      <md-dialog :md-active.sync="logDialogOpened">
        <md-dialog-title>Add Health Record</md-dialog-title>

        <!-- Tab for Add Quick Health Log -->
        <md-tabs md-dynamic-height>
          <md-tab @click="currentTabNumber=0" md-label="Add Quick Health Log">
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
                  >
                    <div v-for="item in healthLogTypes" v-bind:key="item.id">
                      <md-option :value="item.log_type">{{item.log_type}}</md-option>
                    </div>
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

          <!-- Tab for Add Medical Report (Doctor Only) -->
          <md-tab
            v-if="profile.role == 'doctor'"
            @click="currentTabNumber=1"
            md-label="Add Medical Report"
          >
            <!-- Disease Field -->
            <div class="md-layout md-gutter">
              <div class="md-layout-item">
                <md-field>
                  <label for="type">Related Disease</label>
                  <md-input v-model="medicalReportForm.disease" />
                </md-field>
              </div>
            </div>

            <!-- Note Field -->
            <div class="md-layout md-gutter">
              <div class="md-layout-item">
                <md-field>
                  <label for="value">Medical Note</label>
                  <md-input v-model="medicalReportForm.note" />
                </md-field>
              </div>
            </div>
          </md-tab>

          <!-- Tab for Add Medication Reminder (Doctor Only) -->
          <md-tab
            v-if="profile.role == 'doctor'"
            @click="currentTabNumber=2"
            md-label="Add Medication Reminder"
          >
            <!-- Medicine & Disease Field -->
            <div class="md-layout md-gutter">
              <div class="md-layout-item">
                <md-field>
                  <label for="type">Medicine</label>
                  <md-input v-model="medicationReminderForm.medicine" />
                </md-field>
              </div>
              <div class="md-layout-item">
                <md-field>
                  <label for="type">Related Disease</label>
                  <md-input v-model="medicationReminderForm.disease" />
                </md-field>
              </div>
            </div>

            <!-- Amount & Periodicity Field -->
            <div class="md-layout md-gutter">
              <div class="md-layout-item">
                <md-field>
                  <label for="type">Amount</label>
                  <md-input v-model="medicationReminderForm.amount" />
                </md-field>
              </div>
              <div class="md-layout-item">
                <md-field>
                  <label for="type">Periodicity (in hours)</label>
                  <md-input v-model="medicationReminderForm.periodicity" />
                </md-field>
              </div>
            </div>

            <!--  Date Field -->
            <div class="md-layout md-gutter">
              <div class="md-layout-item md-small-size-100">
                <md-field>
                  <label for="date">Start</label>
                  <md-input
                    type="date"
                    id="startDate"
                    name="startDate"
                    v-model="medicationReminderForm.start"
                    :min="currentDate"
                    placeholder=" "
                  />
                </md-field>
              </div>
              <div class="md-layout-item md-small-size-100">
                <md-field>
                  <label for="date">End</label>
                  <md-input
                    type="date"
                    id="endDate"
                    name="endDate"
                    v-model="medicationReminderForm.end"
                    :min="currentDate"
                    placeholder=" "
                  />
                </md-field>
              </div>
            </div>
          </md-tab>
        </md-tabs>

        <md-dialog-actions>
          <md-button class="md-primary" @click="logDialogOpened = false">Cancel</md-button>
          <md-button @click="submitHealthRecord" class="md-primary">Add</md-button>
        </md-dialog-actions>
      </md-dialog>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "action-card",
  data() {
    return {
      patientPhone: null,
      healthLogForm: {
        type: null,
        value: null
      },
      medicalReportForm: {
        disease: null,
        note: null
      },
      medicationReminderForm: {
        disease: null,
        medicine: null,
        amount: null,
        start: null,
        end: null,
        periodicity: null
      },
      setGuestDialogOpened: false,
      logDialogOpened: false,
      currentTabNumber: 0
    };
  },
  computed: {
    ...mapGetters({
      profile: "userProfile",
      healthLogTypes: "healthLogTypes",
      guestProfile: "guestProfile"
    })
  },

  methods: {
    fetchData() {
      this.$store.dispatch("fetchUserProfile");
      this.$store.dispatch("fetchHealthLogTypes");
    },
    openSetGuestDialog() {
      this.setGuestDialogOpened = true;
    },
    openLogDialog() {
      this.currentTabNumber = 0;
      this.logDialogOpened = true;
    },
    submitHealthRecord() {
      if (this.currentTabNumber == 0) {
        this.$store.dispatch("addQuickLog", {
          type: this.healthLogForm.type,
          value: this.healthLogForm.value
        });
      } else if (this.currentTabNumber == 1) {
        this.$store.dispatch("addMedicalReport", {
          disease: this.medicalReportForm.disease,
          note: this.medicalReportForm.note
        });
      } else if (this.currentTabNumber == 2) {
        this.$store.dispatch("addMedicationReminder", {
          medicine: this.medicationReminderForm.medicine,
          disease: this.medicationReminderForm.disease,
          amount: this.medicationReminderForm.amount,
          periodicity: this.medicationReminderForm.periodicity,
          start: this.medicationReminderForm.start,
          end: this.medicationReminderForm.end
        });
      }
      this.logDialogOpened = false;
    },
    clearForm() {
      this.healthLogForm.type = null;
      this.healthLogForm.value = null;
    }
  },
  watch: {
    // Listen to the submission of new guest patient phone number
    patientPhone: function(phone) {
      this.$store.dispatch("fetchUserProfileOf", { phone: phone });
      this.$store.dispatch("fetchHealthLogs", { phone: phone });
      this.$store.dispatch("fetchMedicalReports", { phone: phone });
      this.$store.dispatch("fetchMedicationReminders", { phone: phone });
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
