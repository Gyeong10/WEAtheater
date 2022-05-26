<template>
  <div>
    {{ searchPersonData.name }}
    <br>
    <v-img :src="`https://image.tmdb.org/t/p/w500${searchPersonData.profile_path}`"></v-img>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SearchDataPersonView',
  data() {
    return {
      personPk : this.$route.params.personPk,
    }
  },
  computed: {
    ...mapGetters(['searchPersonData'])
  },
  methods: {
    ...mapActions(['getSearchDataPerson'])
  },
  created() {
    const payload = {personPk : this.personPk}
    this.getSearchDataPerson(payload)
  }
}
</script>

<style>

</style>