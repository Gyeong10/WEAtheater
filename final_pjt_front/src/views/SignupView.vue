<template>
  <div>
    <h1>Signup</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username">Username: </label>
        <input class="inputbox" v-model="credentials.username" type="text" id="username" required />
      </div>
      <div>
        <label for="password1">Password: </label>
        <input class="inputbox" v-model="credentials.password1" type="password" id="password1" required />
      </div>
      <div>
        <label for="password2">Password Comfirmation: </label>
        <input class="inputbox" v-model="credentials.password2" type="password" id="password2" required />
      </div>
      <div>
        <button class="button">가입하기</button>
      </div>
    </form>
  </div>
</template>

<script>
import AccountErrorList from '@/components/AccountErrorList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SignupView',
  components: {
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
    ...mapActions(['signup', 'fetchAuthError'])
  },
  // created() {
  //   this.fetchAuthError()
  // }
}
</script>

<style>

</style>