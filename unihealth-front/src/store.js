import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userProfile: {
      firstName: null,
      lastName: null,
      gender: null,
      birthday: null,
      phone: null,
      role: null
    },
    healthRecords: {
      healthLogTypes: [],
      healthLogs: [],
      medicalReports: [],
      medicationReminders: []
    },
    message: "Welcome to Unihealth!",
    showMessage: false,
    guestProfile: {
      firstName: null,
      lastName: null,
      gender: null,
      birthday: null,
      phone: null,
      role: null
    }
  },
  getters: {
    userProfile(state) {
      return state.userProfile;
    },
    guestProfile(state) {
      return state.guestProfile;
    },
    healthLogTypes(state) {
      return state.healthRecords.healthLogTypes;
    },
    healthLogs(state) {
      return state.healthRecords.healthLogs.reverse();
    },
    medicalReports(state) {
      return state.healthRecords.medicalReports.reverse();
    },
    medicationReminders(state) {
      return state.healthRecords.medicationReminders.reverse();
    },
    message(state) {
      return state.message;
    },
    showMessage(state) {
      return state.showMessage;
    }
  },
  mutations: {
    fetchUserProfile(state) {
      axios.get("/resources/user", {
          headers: {
            Authorization: "Bearer " + localStorage.access_token
          }
        })
        .then(response => {
          state.userProfile = {
            firstName: response.data.first_name,
            lastName: response.data.last_name,
            gender: response.data.gender,
            birthday: response.data.birthday,
            phone: response.data.phone,
            role: response.data.role
          };
        })
        .catch(error => {
          console.log(error);
        });
    },
    fetchUserProfileOf(state, payload) {
      axios.get("/resources/user", {
          headers: {
            Authorization: "Bearer " + localStorage.access_token
          },
          params: {
            phone: payload.phone
          }
        })
        .then(response => {
          state.guestProfile = {
            firstName: response.data.first_name,
            lastName: response.data.last_name,
            gender: response.data.gender,
            birthday: response.data.birthday,
            phone: response.data.phone,
            role: response.data.role
          };

        })
        .catch(error => {
          console.log(error);
          setMessage(state, error.response.data.msg)
        });
    },
    fetchHealthLogTypes(state) {
      axios.get("/resources/health_log_types", {
          headers: {
            Authorization: "Bearer " + localStorage.access_token
          }
        })
        .then(response => {
          state.healthRecords.healthLogTypes = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    addQuickLog(state, payload) {
      axios.post(
          "/resources/health_logs", {
            type: payload.type,
            value: payload.value,
            phone: state.guestProfile.phone
          }, {
            headers: {
              Authorization: "Bearer " + localStorage.access_token
            }
          }
        )
        .then(response => {
          let newLog = {
            log_value: payload.value,
            log_type: payload.type,
            created: new Date().toLocaleString("sv-SE")
          };
          state.healthRecords.healthLogs.push(newLog);
          setMessage(state, response.data.msg)

        })
        .catch(error => {
          console.log(error);
          setMessage(state, error.response.data.msg)
        });
    },
    addMedicalReport(state, payload) {
      axios.post(
          "/resources/medical_reports", {
            disease: payload.disease,
            note: payload.note,
            phone: state.guestProfile.phone
          }, {
            headers: {
              Authorization: "Bearer " + localStorage.access_token
            }
          }
        )
        .then(response => {
          let newReport = {
            disease: payload.disease,
            note: payload.note,
            created: new Date().toLocaleString("sv-SE"),
            id: response.data.reportId
          };
          state.healthRecords.medicalReports.push(newReport);
          setMessage(state, response.data.msg)
        })
        .catch(error => {
          console.log(error);
          setMessage(state, error.response.data.msg)
        });
    },
    addMedicationReminder(state, payload) {
      axios.post(
          "/resources/medication_reminders", {
            disease: payload.disease,
            medicine: payload.medicine,
            amount: payload.amount,
            periodicity: payload.periodicity,
            start: payload.start,
            end: payload.end,
            phone: state.guestProfile.phone,
          }, {
            headers: {
              Authorization: "Bearer " + localStorage.access_token
            }
          }
        )
        .then(response => {
          setMessage(state, response.data.msg)
        })
        .catch(error => {
          console.log(error);
          setMessage(state, error.response.data.msg)
        });
    },
    fetchHealthLogs(state, payload) {
      axios.get("/resources/health_logs", {
          headers: {
            Authorization: "Bearer " + localStorage.access_token
          },
          params: {
            phone: payload ? payload.phone : null
          }
        })
        .then(response => {
          state.healthRecords.healthLogs = response.data.map(log => {
            log.created = new Date(log.created).toLocaleString("sv-SE");
            return log;
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    fetchMedicalReports(state, payload) {
      axios.get("/resources/medical_reports", {
          headers: {
            Authorization: "Bearer " + localStorage.access_token
          },
          params: {
            phone: payload ? payload.phone : null
          }
        })
        .then(response => {
          state.healthRecords.medicalReports = response.data.map(log => {
            log.created = new Date(log.created).toLocaleString("sv-SE");
            return log;
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    fetchMedicationReminders(state, payload) {
      axios.get("/resources/medication_reminders", {
          headers: {
            Authorization: "Bearer " + localStorage.access_token
          },
          params: {
            phone: payload ? payload.phone : null
          }
        })
        .then(response => {
          state.healthRecords.medicationReminders = response.data.map(log => {
            log.created = new Date(log.created).toLocaleString("sv-SE");
            return log;
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    resetState(state) {
      state.userProfile = {
        firstName: null,
        lastName: null,
        gender: null,
        birthday: null,
        phone: null,
        role: null
      };
      state.guestProfile = {
        firstName: null,
        lastName: null,
        gender: null,
        birthday: null,
        phone: null,
        role: null
      };
      state.healthRecords = {
        healthLogTypes: [],
        healthLogs: [],
        medicalReports: []
      };
      state.message = "Welcome to Unihealth!";
      state.showMessage = false
    }
  },
  actions: {
    fetchUserProfile(context) {
      context.commit('fetchUserProfile')
    },
    fetchUserProfileOf(context, payload) {
      context.commit('fetchUserProfileOf', payload)
    },
    fetchHealthLogTypes(context) {
      context.commit('fetchHealthLogTypes')
    },

    fetchHealthLogs(context, payload) {
      context.commit('fetchHealthLogs', payload);
    },
    fetchMedicalReports(context, payload) {
      context.commit('fetchMedicalReports', payload);
    },
    fetchMedicationReminders(context, payload) {
      context.commit('fetchMedicationReminders', payload);
    },
    addQuickLog(context, payload) {
      context.commit('addQuickLog', payload)
    },
    addMedicalReport(context, payload) {
      context.commit('addMedicalReport', payload)
    },
    addMedicationReminder(context, payload) {
      context.commit('addMedicationReminder', payload)

    }
  }
});

function setMessage(state, msg) {
  state.message = msg;
  state.showMessage = true;
  setTimeout(() => {
    state.showMessage = false
  }, 4000)
}
