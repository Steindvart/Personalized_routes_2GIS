<template>
  <div>
    <h2>Пример интеграции карты 2GIS</h2>
    <h3>Выбранные координаты</h3>
    <p>Широта: {{ selectedPoint[0] }}, Долгота: {{ selectedPoint[1] }}</p>
    <div class="map-container">
      <t-gis-map
        :center="[82.89785, 54.98021]"
        :styles="{width: '100%', height: '100%'}"
        :zoom="12"
        :enableCircle="true"
        :radius="1500"
        :selectedPoint="selectedPoint"
      ></t-gis-map>
    </div>
    <h2>Запрос к справочнику 2GIS о Новосибирских кофейнях</h2>
    <div class="info-container">
      <ul v-if="items.length">
        <li v-for="item in items" :key="item.id">
          "{{ item.name }}", {{ item.address_name }}
        </li>
      </ul>
      <p v-else>Loading...</p>
    </div>
  </div>
</template>

<script>
import tGisMap from '@/components/tGisMap'
import { ref, onMounted } from 'vue'

export default {
  name: 'mapPage',
  components: {
    tGisMap
  },

  setup() {
    const items = ref([])
    const selectedPoint = ref([0, 0])

    const fetchData = async () => {
      try {
        const apiKey = useRuntimeConfig().public.tGisApiKey
        const url = 'https://catalog.api.2gis.com/3.0/items';
        const query = `q=Новосибирск кафе&type=branch&page_size=10&page=1&key=${apiKey}`
        const response = await fetch(`${url}?${query}`)
        const data = await response.json()
        items.value = data.result.items
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    }

    onMounted(() => {
      fetchData()
    })

    return {
      items,
      selectedPoint
    }
  }
}
</script>

<style scoped>
.map-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  width: 100%;
}

.map-container > div {
  flex-grow: 1;
  height: 100%;
}

.info-container {
  margin-top: 20px;
  padding: 20px;
  background-color: #f5f5f5;
}
</style>
