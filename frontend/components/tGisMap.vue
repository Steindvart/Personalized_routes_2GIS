<template>
  <div>
    <div id="2GisMap" :style="styles"></div>
  </div>
</template>

<script>
  import { load } from '@2gis/mapgl';

  export default {
    props: {
      center: {
        type: Array,
        default: []
      },
      marker: {
        type: Array,
        default: []
      },
      zoom: {
        type: Number,
        default: 13
      },
      styles: {
        type: Object,
        default: () => {
          return {width: '100%', height: '100%'}
        }
      }
    },

    methods: {
      async start() {
        const mapglAPI = await load();
        const apiKey = useRuntimeConfig().public.tGisApiKey

        const map = new mapglAPI.Map('2GisMap', {
            center: this.center,
            zoom: this.zoom,
            key: apiKey,
        });

        const marker = new mapglAPI.Marker(map, {
            coordinates: this.marker,
        });
      }
    },

    created() {
      this.start();
    }
  }
</script>