<template>
  <div>

    <v-container>
    <v-row dense>
    <v-col cols="12" class="my-3">
    <v-card
      color="#dbcfb071"
      class="rounded-pill"
    >
    <div id="recommend">
      <h2><i class=" fa fa-duotone fa-user-astronaut"></i> {{ currentUser.username }}님이 좋아하는 배우 출연 영화 </h2>
        <div v-if="actorRecom" id="card">
          <swiper ref="filterSwiper" :options="swiperOption" role="tablist">
          <swiper-slide role="tab">
          <recommend-movie-card
            v-for="(movie, idx) in actorRecom" :key="idx" :allMovie="movie"
          >
          </recommend-movie-card>
          </swiper-slide>
        </swiper>
        </div>
    </div>
    </v-card>
    </v-col>
    </v-row>
    </v-container>
  </div>
</template>


<script>
import RecommendMovieCard from '@/components/HomeView/RecommendMovieCard'
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'

import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'RecommendActor',
  components: { swiper,
    swiperSlide, RecommendMovieCard },
  data () {
    return {
      swiperOption: {
        slidesPerView: 'auto',
        spaceBetween: 10, // swiper-slide 사이의 간격 지정
        slidesOffsetBefore: 50, // slidesOffsetBefore는 첫번째 슬라이드의 시작점에 대한 변경할 때 사용
        slidesOffsetAfter: 100, // slidesOffsetAfter는 마지막 슬라이드 시작점 + 마지막 슬라이드 너비에 해당하는 위치의 변경이 필요할 때 사용
        freeMode: true, // freeMode를 사용시 스크롤하는 느낌으로 구현 가능
        centerInsufficientSlides: true, // 컨텐츠의 수량에 따라 중앙정렬 여부를 결정함
      }
    }
  },
  computed: {
    ...mapGetters(['actorRecom', 'currentUser']),
  },
  methods: {
    ...mapActions(['getActorRecom']),
  },
  created() {
    this.getActorRecom()
  }
}

</script>

<style lang="scss" scoped>
#recommend {
  white-space:nowrap; 
  overflow-x: hidden; 
  text-align:center;
  padding: 3vh 0;
}
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
      background: #dbcfb000;
      appearance: none;
      cursor: pointer;
    }
  }
}
.middle {
  align-items: center;
}
h2 {
  color: white;
}
</style>