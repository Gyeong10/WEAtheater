<template>
  <form @submit.prevent="onSubmit">
    <div>
      <label for="title">제목: </label>
      <input v-model="newArticle.title" type="text" id="title" required>
    </div>
    <div>
      게시판 선택
        <Dropdown
          :options="options"
          @selected="validateSelection"
          :disabled="false"
          name="category"
          :maxItem="10"
          placeholder="Please select an option"
          >
      </Dropdown>
    </div>
    <div>
      <label for="content">내용: </label>
      <textarea v-model="newArticle.content" type="text" id="content" required></textarea>
    </div>
    <div>
      <button>{{ action }}</button>
    </div>
  </form>
</template>

<script>
import Dropdown from 'vue-simple-search-dropdown'
import { mapActions } from 'vuex'

export default {
  name: 'ArticleForm',
  props: {
    article: Object,
    action: String,
  },
  components: { Dropdown },
  data() {
    return {
      newArticle: {
        title: this.article.title,
        content: this.article.content,
        category: this.article.category
      },
      options: [
        { name: "자유게시판", id: 2 },
        { name: "영화게시판", id: 3 },
      ],
      // selected: { name: null, id: null },

    }
  },

  methods: {
    ...mapActions(['createArticle', 'updateArticle']),
    onSubmit() {
      // console.log(this.newArticle)
      if (this.action === 'create') {
        this.createArticle(this.newArticle)
      } else if (this.action === 'update') {
        const payload = {
          pk: this.article.pk,
          ...this.newArticle,
        }
        this.updateArticle(payload)
      }
    },
    validateSelection(selection) {
      // console.log(selection)
      this.newArticle.category = selection.id
    },
  },
}
</script>

<style>

</style>