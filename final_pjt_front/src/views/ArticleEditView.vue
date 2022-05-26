<template>
  <div>
    <article-form v-if="isArticle" :article="article" :action="action">
      
    </article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/CommunityView/ArticleForm'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ArticleEditView',
  components: { ArticleForm },
  data () {
    return {
      action: "UPDATE"
    }
  },
  computed: {
    ...mapGetters(['article', 'isArticle']),
  },
  methods: {
    ...mapActions(['fetchArticle']),
  },
  created() {
    this.fetchArticle(this.$route.params.articlePk)
  },
}
</script>

<style>

</style>