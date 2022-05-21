<template>
  <div>
    <h1>Signup</h1>
    <account-error-list v-if="authError"></account-error-list>
    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username">Username: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>
      <div>
        <label for="password1">Password: </label>
        <input v-model="credentials.password1" type="text" id="password1" required />
      </div>
      <div>
        <label for="password2">Password: </label>
        <input v-model="credentials.password2" type="text" id="password2" required />
      </div>
      <div>
        <button>가입하기</button>
      </div>
    </form>
  </div>
</template>

<script>
import AccountErrorList from '@/components/AccountErrorList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SignupView',
  component: {
    AccountErrorList,
  },
  data () {
    return {
      credentials: {
        username: '',
        password1: '',
        password2: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup'])
  }
}
</script>

<style>

</style>