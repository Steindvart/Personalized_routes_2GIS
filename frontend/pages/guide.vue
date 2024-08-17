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
            <div v-if="isochroneData">
                <pre>{{ isochroneData }}</pre>
            </div>
        </v-card>
    </v-container>
  </div>
    
</template>


<script>
import infoCard from '../components/infoGPTCard'
import axios from 'axios'

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
  methods: {
    async getIsochroneData(coordinates) {
    //   this.mapCenter = [coordinates.latitude, coordinates.longitude],
    //   this.deltatime = coordinates.radius 
      try {
        const apiKey = 'YOUR_API_KEY'; // Replace with your actual API key
        const isoUrl = `https://routing.api.2gis.com/2.0/isochrone?key=${apiKey}`;

        const requestData = {
          start: {
            lat: coordinates.latitude,
            lon: coordinates.longitude
          },
          durations: [coordinates.radius*60],       // Time in seconds (e.g., 10 and 20 minutes)
          mode: 'walking'               // Can be 'driving', 'bicycling', or 'pedestrian'
        };

        const response = await axios.post(isoUrl, requestData, {
          headers: {
            'Content-Type': 'application/json'
          }
        });

        console.log('Isochrone Data:', response.data);  // Handle the response data
        this.isochroneData = response.data;

      } catch (error) {
        console.error('Error fetching isochrone data:', error);
      }
    },
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