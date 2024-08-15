<template>
  <v-container class="full-width-container">
    <h1>Умные путешествия</h1>
    <br/>
    <div class="content-wrapper">
      <route-info-card
        class="settings-card"
        :items="items"
      >
      </route-info-card>
      <v-card class="map-container" outlined>
        <template v-slot:title>
          <span class="font-weight-black">Навигация</span>
        </template>
        <v-card-text>
          <t-gis-map
            :center="[82.89785, 54.98021]"
            :styles="{width: '100%', height: '870px'}"
            :zoom="12"
          ></t-gis-map>
        </v-card-text>
      </v-card>
    </div>
    <br/>
  </v-container>
</template>


<script>
import routeInfoCard from '@/components/routeInfoCard'

export default {
  name: 'routePage',
  components: {
    routeInfoCard
  },

  data: () => ({
    items: [
      {
        color: 'red-lighten-2',
        icon: 'mdi-star',
        name: 'Стартовая точка',
        desc: ""
      },
      {
        color: 'red-lighten-2',
        icon: 'mdi-star',
        name: 'Кафе "Плюшка"',
        desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
      },
      {
        color: 'purple-lighten-2',
        icon: 'mdi-book-variant',
        name: 'Парк "Красивый"',
        desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
      },
      {
        color: 'green-lighten-1',
        icon: 'mdi-airballoon',
        name: 'Караоке "Певун"',
        desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
      },
    ],
  }),
}
</script>

<style scoped>
.full-width-container {
  max-width: 100% !important; /* Убираем ограничение по ширине */
  width: 100%; /* Занимаем всю ширину экрана */
  padding: 0; /* Убираем лишние отступы */
}

.content-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: stretch;
}

.settings-card {
  flex: 1 1 60%; /* Гибкий размер, 60% ширины от родителя */
  margin-right: 16px; /* Отступ между картой и настройками */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

.map-container {
  flex: 2 1 70%; /* Гибкий размер, 70% ширины от родителя */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  height: 100%; /* Занимает всю высоту родителя */
  display: flex; /* Гарантируем, что вложенные элементы будут растягиваться */
  flex-direction: column;
}

.map-container > .v-card-text {
  flex-grow: 1; /* Внутренний контент растягивается */
  padding: 0; /* Убираем лишние отступы */
}

.t-gis-map {
  width: 100%;
  height: 100%;
}
</style>
