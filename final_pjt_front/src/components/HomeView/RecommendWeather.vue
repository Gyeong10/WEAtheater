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
        <h2><i :class="`fa ${this.matchIcon[weatherIcon[0].icon]}`"></i> {{this.matchDesc[weatherIcon[0].main]}} </h2>
        <swiper ref="filterSwiper" class="middle" :options="swiperOption" role="tablist">
          <swiper-slide role="tab">
            <recommend-movie-card
              v-for="(movie, idx) in weatherRecom" :key="idx" :allMovie="movie"
            >
            </recommend-movie-card>
          </swiper-slide>
        </swiper>
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
  name: 'RecommendWeather',
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
      },
      matchIcon: {
        '01d': 'fa-sun',
        '02d': 'fa-cloud-sun',
        '03d': 'fa-cloud',
        '04d': 'fa-cloud',
        '09d': 'fa-cloud-showers-heavy',
        '10d': 'fa-umbrella',
        '11d': 'fa-cloud-bolt',
        '13d': 'fa-snowflake',
        '50d': 'fa-smog',

        '01n': 'fa-moon',
        '02n': 'fa-cloud-moon',
        '03n': 'fa-cloud',
        '04n': 'fa-cloud',
        '09n': 'fa-cloud-showers-heavy',
        '10n': 'fa-cloud-rain',
        '11n': 'fa-cloud-bolt',
        '13n': 'fa-snowflake',
        '50n': 'fa-smog',
      },
      matchDesc: {
        'Thunderstorm': '쿠르릉 쾅! 번개치는 날에 볼만한 영화',
        'Drizzle': '보슬보슬 비가 내리는 날에 보기 좋은 영화',
        'Rain': '주륵주륵 비가 내리는 날에 추천하는 영화',
        'Snow': '소복소복 눈이 쌓이는 날에 봐야하는 영화',

        'Mist': '안개가 자욱한 날에는 이런 영화 어때요?',
        'Smoke': '도망가세요!',
        'Haze': '실안개 낀 으스스한 날에 볼 영화',
        'Fog': '한치 앞도 안보이는 날에 추천하는 영화',
        'Sand': '모래바람..?',
        'Ash': '한국에 이런 날씨가 있을까요?',
        'Squall': '돌풍이 부는 날엔 집에서...',
        'Tornado': '토네이도가 치면 도망가세요',

        'Clear': '놀러가고 싶은 맑은 날씨에 추천하는 영화',
        'Clouds': '구름이 많아 우중충한 날 집에서 볼만한 영화',
      }
    }
  },
  computed: {
    ...mapGetters(['weatherRecom', 'currentUser', 'weatherIcon']),
  },
  methods: {
    ...mapActions(['getWeatherRecom', 'getWeatherIcon']),
  },
  created() {
    this.getWeatherRecom()
    this.getWeatherIcon()
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