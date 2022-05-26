<template>
<div>
  <div class="card d-flex">

    <div>
      <div class="title">
        <h1 class="d-inline font">
          {{ searchPersonData.name }}
        </h1>
      <h3 class="my-3">Information</h3>
      <div class="box">
        출생 : {{ searchPersonData.birthday }}
        <br>
        성별 : {{ gender[searchPersonData.gender] }}
      </div>
    </div>
    <v-btn 
      @click="goBack"
      outlined
      id="btn"
    >Main</v-btn>
    </div>

    <div>
      <v-card
          class="mx-auto rounded-xl"
          max-width="600"
        >
        <v-img
          class="rounded-t-xl"
          height="1000"
          :src="`https://image.tmdb.org/t/p/w500${searchPersonData.profile_path}`"
        >
        </v-img>
        </v-card>
    </div>
  </div>
</div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SearchDataPersonView',
  data() {
    return {
      personPk : this.$route.params.personPk,
      gender: {
        '1': '여성',
        '2': '남성',
      },
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

<style scoped>

.img {
  height: 33rem;
}
.title {
  width: 50vw;
  margin: 1vh 3vw;
  line-height: 150%;
}
.font {
  font-family: 'Hahmlet', serif;
}
#btn {
  color: #dbcfb0;
}
</style>