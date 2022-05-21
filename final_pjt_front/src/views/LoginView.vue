<template>
  <div>
    <h1>Login</h1>
    <account-error-list v-if="authError"></account-error-list>
    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">Username: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>
      <div>
        <label for="password">Password: </label>
        <input v-model="credentials.password1" type="text" id="password" required />
      </div>
      <div>
        <button>Login</button>
      </div>
    </form>
  </div>
</template>

<script>
import AccountErrorList from '@/components/AccountErrorList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'LoginView',
  component: {
    AccountErrorList,
  },
  data () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login'])
  }
}
</script>

<style>

</style>