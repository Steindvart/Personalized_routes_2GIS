<template>
  <div> 
    <h2>GPT-основанный гайд</h2>
    <v-container class="content_wrapper">
        <info-card class="info_card">    
        </info-card>
        <v-card class="map_container">
          <template v-slot:title>
              <span class="font-weight-black">Карта</span>
          </template>
          <info-gpt-card @fetch-isochrone="getIsochroneData"></info-gpt-card>
          <v-card-text>
            <t-gis-map
              :center="[82.89785, 54.98021]"
              :styles="{width: '100%', height: '870px'}"
              :zoom="12"
              :selectedPoint="selectedPoint"
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
      isochroneData: null, // To store the API response
    }
  },
  setup() {
    const selectedPoint = ref([0, 0])

    return { selectedPoint }
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
  margin-right: 16px; /* Отступ между картой и настройками */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #fff;

}
.map_container {
  flex: 2 1 60%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  height: 100%; /* Занимает всю высоту родителя */
  display: flex; /* Гарантируем, что вложенные элементы будут растягиваться */
  flex-direction: column;
}

</style>