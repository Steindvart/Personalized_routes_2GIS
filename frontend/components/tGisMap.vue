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
          return {width: '500px', height: '400px'}
        }
      }
    },

    methods: {
      async start() {
        const mapglAPI = await load();

        const map = new mapglAPI.Map('2GisMap', {
            center: this.center,
            zoom: this.zoom,
            key: '333f2738-8ebc-482c-8f34-d438836ca445',
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