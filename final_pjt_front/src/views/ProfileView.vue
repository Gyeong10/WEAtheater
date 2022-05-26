<template>
  <div>
    <h1>{{ profile.username }}'s PROFILE</h1>
    <h2><i class="fa fa-heart"></i> 관심있는 영화</h2>
    <ul>
      <swiper ref="filterSwiper" class="middle" :options="swiperOption" role="tablist">
        <swiper-slide role="tab">
      <v-container class="d-flex">
      <movie-card
        v-for="(movie, idx) in profile.like_movies" :key="idx" :allMovie="movie"
      >
      </movie-card>
      </v-container>
      </swiper-slide>
      </swiper>
    </ul>
    <br>
    <h2>작성한 글</h2>
    <div class="box">
      <ul>
        <li v-for="(article, idx) in profile.articles" :key="idx" class="d-flex justify-space-between">
          <div class="ms-10">
            {{ idx+1 }}
          </div>
            <router-link class="link" :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.title }}
            </router-link>
          <div>
          {{ article.created_at }}
          </div>
        </li>
      </ul>
    </div>
    <br>
    <h2>작성한 댓글</h2>
    <div class="box">
      <ul>
        <li v-for="(comment, idx) in profile.comments" :key="idx" class="d-flex justify-space-between">
          <div class="ms-10">
            {{ idx + 1 }}
          </div>
        <router-link class="link" :to="{ name: 'article', params: { articlePk: comment.article } }">
          {{ comment.content }}
        </router-link>
        <div>
          {{ comment.created_at }}
        </div>
      </li>
    </ul>
    </div>
    <br>
    <h2>좋아요 누른 게시글</h2>
    <div class="box">
      <ul>
      <li v-for="(article, idx) in profile.like_articles" :key="idx" class="d-flex justify-space-between">
          <div class="ms-10">
            {{ idx+1 }}
          </div>
        <router-link class="link" :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      <div>
          {{ article.created_at }}
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MovieCard from '@/components/MovieListView/MovieCard'
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'


export default {
  name: 'ProfileView',
  components: { MovieCard, swiper,
    swiperSlide },
    data () {
    return {
      swiperOption: {
        slidesPerView: 'auto',
        spaceBetween: 10, // swiper-slide 사이의 간격 지정
        slidesOffsetBefore: 10, // slidesOffsetBefore는 첫번째 슬라이드의 시작점에 대한 변경할 때 사용
        slidesOffsetAfter: 200, // slidesOffsetAfter는 마지막 슬라이드 시작점 + 마지막 슬라이드 너비에 해당하는 위치의 변경이 필요할 때 사용
        freeMode: true, // freeMode를 사용시 스크롤하는 느낌으로 구현 가능
        centerInsufficientSlides: true, // 컨텐츠의 수량에 따라 중앙정렬 여부를 결정함
      }
    }
  },
  computed: {
    ...mapGetters(['profile'])
  },
  methods : {
    ...mapActions(['fetchProfile'])
  },
  created () {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  }
}
</script>

<style lang="scss" scoped>
.swiper-container {
  .swiper-wrapper {
    .swiper-slide {
      width: auto; // auto 값을 지정해야 슬라이드의 width값이 텍스트 길이 기준으로 바뀜
      min-width: 56px; // min-width를 지정하지 않을 경우 텍스트가 1개 내지는 2개가 들어갈 때 탭 모양이 상이할 수 있으므로 넣어준다.
      padding: 0px 14px;
      font-size: 14px;
      line-height: 36px;
      text-align: center;
      color: #84868c;
      border: 0;
      border-radius: 18px;
      background: black;
      appearance: none;
      cursor: pointer;
    }
  }
}
h2 {
  text-align: left;
  margin: auto 6vw;
}
li {
  list-style: none;
}
.link {
  color: white;
}
.box {
  border: 1px solid #dbcfb0;
  margin: 1vh 5vw;
  padding: 5px 8px;
  border-radius: 10px;
  color: #dbcfb0;
  line-height: 200%;
  min-height: 45px;
}
</style>