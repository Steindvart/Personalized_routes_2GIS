<template>
  <div>
    <h1>Твой личный гид</h1>
    <v-container class="content_wrapper">
      <info-card
        class="info_card"
        :point="selectedPoint"
        :radius="radius"
        :loading="loading"
        :story="story"
        @fetch-story="fetchStory"
      />
      <v-card class="map_container">
        <template v-slot:title>
          <span class="font-weight-black">Карта</span>
          <p class="coordinates_field">Широта: {{ selectedPoint[0] }}, Долгота: {{ selectedPoint[1] }}, Радиус: {{ radius }}</p>
        </template>
        <v-card-text>
          <t-gis-map
            :center="[82.89785, 54.98021]"
            :styles="{width: '100%', height: '870px'}"
            :zoom="12"
            :selectedPoint="selectedPoint"
            :enableCircle="true"
            :radius="radius"
            @radius-updated="updateMapData">
          ></t-gis-map>
        </v-card-text>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import infoCard from '../components/infoGPTCard'
import axios from 'axios'
import { ref } from 'vue'

export default {
  name: 'indexPage',
  components: {
    infoCard
  },
  data() {
    return {
      radius: 1000,
      loading: false,
      story: null,
    }
  },
  setup() {
    const selectedPoint = ref([0, 0])
    return { selectedPoint }
  },
  methods: {
    updateMapData({ radius }) {
      this.radius = radius;
    },
    async fetchStory() {
      this.loading = true;
      try {
        const response = await axios.get(`http://localhost:8000/api/guide/story/find?lon=${this.selectedPoint[0]}&lat=${this.selectedPoint[1]}&radius=${this.radius}`);
        this.story = response.data.content;
      } catch (error) {
        console.error("Error fetching story:", error);
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>

<style scoped>
.content_wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: stretch;
}

.info_card {
  flex: 1 1 30%;
  margin-right: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}
.map_container {
  flex: 2 1 70%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  height: 100%;
  display: flex;
  flex-direction: column;
}

.coordinates_field {
  font-size: 14px;
  height: 20px;
}
</style>
