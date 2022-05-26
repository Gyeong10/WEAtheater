<template>
  <div class="loginbody">
    <h1>LOGIN</h1>
    
    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">Username: </label>
        <input class="inputbox" v-model="credentials.username" type="text" id="username" required />
      </div>
      <div>
        <label for="password">Password: </label>
        <input class="inputbox" v-model="credentials.password" type="password" id="password" required />
      </div>
      <br>
      <account-error-list v-if="authError"></account-error-list>
      <div>
        <button class="button">Login</button>
      </div>
    </form>
  </div>
</template>

<script>
import AccountErrorList from '@/components/AccountErrorList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'LoginView',
  components: {
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
    ...mapActions(['login', 'fetchAuthError'])
  },
  // created() {
  //   this.fetchAuthError()
  // }
}
</script>

<style>

.loginbody {
  padding: 70px 0;
}
</style>