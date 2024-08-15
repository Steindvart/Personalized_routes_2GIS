<template>
  <v-container>
    <v-card outlined>
      <v-card-text>
        <div>
          <h1 class="headline font-weight-bold">Умные путешествия</h1>
          <h2 class="subheadline font-weight-light">Сервис подбора персональных маршрутов для небольших путешествий</h2>
        </div>
        <p class="description mt-4">
          🤔 Не знаешь куда сходить? Надоели одни и те же места, но не хочешь нарваться на то, что тебе точно не понравится?
        </p>
        <p class="description mt-3">
          ✨ Наш сервис избавит тебя от этих проблем! Выбери свои постоянные предпочтения, укажи чем ты хочешь заняться и сервис построит тебе мини-путешествие из мест, которые подходят под твои предпочтения и обладают высоким рейтингом.
        </p>
        <p class="description mt-3">
          🤖 И это не всё! В этом путешествии тебя будет сопровождать ИИ-ассистент, который как опытный гид будет с юмором рассказывать истории об интересных местах поблизости.
        </p>
        <v-row class="my-5">
          <v-btn
            color="primary"
            @click="goToPreferences"
            class="mx-4"
            rounded="xl"
            size="large"
            large
          >
            Настроить постоянные предпочтения
          </v-btn>
          <v-btn color="green" @click="goToRouteGenerator" rounded="xl" size="large" large>Настроить маршрут</v-btn>
        </v-row>
      </v-card-text>
    </v-card>
    <br/>
    <h2>Пример построенного путешествия</h2>
    <div class="content-wrapper">
      <route-info-card
        class="settings-card"
        :items="items"
      >
      </route-info-card>
      <v-card class="map-container" subtitle="Оптимальный путь вашего мини-путешествия :)" outlined>
        <template v-slot:title>
          <span class="font-weight-black">Навигация</span>
        </template>
        <v-card-text>
          <t-gis-map
            :center="[82.89785, 54.98021]"
            :styles="{width: '100%', height: '870px'}"
            :zoom="14"
            :enableMarker="false"
          ></t-gis-map>
        </v-card-text>
      </v-card>
    </div>
  </v-container>
</template>

<script>
import routeInfoCard from '@/components/routeInfoCard'

export default {
  components: {
    routeInfoCard
  },
  methods: {
    goToPreferences() {
      this.$router.push('/preferences');
    },
    goToRouteGenerator() {
      this.$router.push('/generator');
    }
  },

  data: () => ({
    items: [
      {
        type: 'start',
        name: 'Стартовая точка',
        desc: "",
        rating: null,
        point: [82.89821282451898, 54.98018285867834]
      },
      {
        type: 'food',
        name: 'Кафе "Плюшка"',
        desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        rating: 4.3,
        point: [82.90568931600684, 54.983789907034286]
      },
      {
        type: 'walk',
        name: 'Сквер им. Сибиряков-Гвардейцев',
        desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        rating: null,
        point: [82.8904133554231, 54.97939911412844]
      },
      {
        type: 'fun',
        name: 'Караоке "Певун"',
        desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        rating: 4.5,
        point: [82.9115555313026, 54.99266076608315]
      },
      {
        type: 'walk',
        name: 'Парк "Арена"',
        desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        rating: null,
        point: [82.92598203704318, 54.99680146158085]
      },
    ],
  }),
}
</script>

<style scoped>
.headline {
  font-size: 2.3rem;
  color: #222222;
}

.subheadline {
  font-size: 1.4rem;
  color: #444444;
}

.description {
  font-size: 1rem;
  line-height: 1.5;
  color: #383838;
  font-family: 'Roboto', sans-serif;
  max-width: 1000px;
}

v-divider {
  margin: 20px 0;
}

v-btn {
  font-size: 1rem;
  text-transform: none;
}

.content-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: stretch;
}

.settings-card {
  flex: 1 1 60%;
  margin-right: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

.map-container {
  flex: 2 1 70%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  height: 100%;
  display: flex;
  flex-direction: column;
}

.map-container > .v-card-text {
  flex-grow: 1;
  padding: 0;
}

.t-gis-map {
  width: 100%;
  height: 100%;
}
</style>
