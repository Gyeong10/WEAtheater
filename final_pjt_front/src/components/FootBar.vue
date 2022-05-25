<template>
  <v-footer
    class="footer"
    color="#DBCFB0"
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        v-for="link in links"
        :key="link"
        color="#545775"
        text
        rounded
        class="my-2"
      >
        {{ link }}
      </v-btn>
      <v-col
        class="#545775 py-4 text-center dark--text"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Lee JuYeong | Park GeongYeol</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>


<script>
  export default {
    data: () => ({
      links: [
        'Home',
        'About Us',
        'Services',
        'NOTION',
        'Contact Us',
      ],
    }),
  }
</script>

<style>
.footer {
  height: 100px;
  position : absolute;
  bottom: 0;
}
</style>