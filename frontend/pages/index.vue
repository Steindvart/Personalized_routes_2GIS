<template>
  <v-container>
    <h1>Умные путешествия</h1>
    <br/>
    <div class="content-wrapper">
      <route-settings-card class="settings-card"></route-settings-card>
      <div class="map-container">
        <t-gis-map
          :center="[82.89785, 54.98021]"
          :styles="{width: '100%', height: '100%'}"
          :zoom="12"
          :selectedPoint="selectedPoint"
        ></t-gis-map>
      </div>
    </div>
    <br/>
  </v-container>
</template>


<script>
import routeSettingsCard from '@/components/routeSettingsCard'

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
.content-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: stretch;
}

.settings-card {
  flex: 1 1 50%; /* Гибкий размер, 30% ширины от родителя */
  margin-right: 16px; /* Отступ между картой и настройками */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  padding: 16px;
  border-radius: 8px;
}

.map-container {
  flex: 2 1 70%; /* Гибкий размер, 70% ширины от родителя */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.map-container > div {
  width: 100%;
  height: 100%;
}
</style>
