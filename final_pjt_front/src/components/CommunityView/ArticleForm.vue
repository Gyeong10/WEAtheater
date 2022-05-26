<template>
  <div>
    <router-link class="link smallButton" id="router" :to="{ name: 'community', params: { category: 'all' } }">목록</router-link>
    <div class="articleform">
      <form @submit.prevent="onSubmit">
        <div class="d-flex mx-auto">
          <h5 class="d-inline">게시판 선택</h5>
          
            <Dropdown
              :options="options"
              @selected="validateSelection"
              :disabled="false"
              name="category"
              :maxItem="10"
              placeholder="Please select an option"
              class="d-inline mx-2"
              >
          </Dropdown>
        </div>
        <div>
          <label for="title">제목</label>
          <input class="inputbox" v-model="newArticle.title" type="text" id="title" required>
        </div>
        <div class="d-flex ms-8">
          <label for="content">내용</label>
          <textarea class="inputbox" v-model="newArticle.content" type="text" id="content" required></textarea>
        </div>
        <div>
          <button class="button">{{ action }}</button>
        </div>
      </form>
    </div>
  </div>
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
      if (this.action === 'CREATE') {
        this.createArticle(this.newArticle)
      } else if (this.action === 'UPDATE') {
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

<style scoped>
.articleform {
  background-color: #fff9e9;
  color: #545775;
  height: 70vh;
  padding: 5vh;
  margin: 5vh;
}
.inputbox {
  color: #545775;
}
#title {
  width: 80vw;
  margin: 2vh;
}

#content {
  width: 80vw;
  height: 35vh;
  margin: 2vh;
}
.link {
  color: #545775
}

</style>