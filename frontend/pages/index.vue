<template>
  <v-container class="full-width-container">
    <h1>Умные путешествия</h1>
    <br/>
    <div class="content-wrapper">
      <route-settings-card class="settings-card"></route-settings-card>
      <v-card class="map-container" subtitle="Укажи маркер на карте – *тык*" outlined>
        <template v-slot:title>
          <span class="font-weight-black">Место от которого будем искать</span>
        </template>
        <v-card-text>
          <t-gis-map
            :center="[82.89785, 54.98021]"
            :styles="{width: '100%', height: '765px'}"
            :zoom="12"
            :selectedPoint="selectedPoint"
          ></t-gis-map>
        </v-card-text>
      </v-card>
    </div>
    <br/>
  </v-container>
</template>


<script>
import routeSettingsCard from '@/components/routeSettingsCard'
import { ref } from 'vue'

export default {
  name: 'indexPage',
  components: {
    routeSettingsCard
  },

  setup() {
    const selectedPoint = ref([0, 0])

    return { selectedPoint }
  }
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
