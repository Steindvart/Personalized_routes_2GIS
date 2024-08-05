<template>
  <div>
    <div id="2GisMap" :style="styles"></div>
  </div>
</template>

<script>
  import { load } from '@2gis/mapgl';

  const config = useRuntimeConfig()

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
          return {width: '800px', height: '600px'}
        }
      }
    },

    methods: {
      async start() {
        const mapglAPI = await load();

        const map = new mapglAPI.Map('2GisMap', {
            center: this.center,
            zoom: this.zoom,
            key: config.tGisApiKey,
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