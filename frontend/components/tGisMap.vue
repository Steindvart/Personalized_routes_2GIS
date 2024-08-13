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
        default: () => [82.89785, 54.98021],
      },
      zoom: {
        type: Number,
        default: 13
      },
      radius: {
        type: Number,
        default: 500,
      },
      enableCircle: {
        type: Boolean,
        default: false
      },
      selectedPoint: {
        type: Array,
        default: () => [0, 0],
      },
      styles: {
        type: Object,
        default: () => {
          return {width: '100%', height: '100%'}
        }
      }
    },

    data() {
      return {
        map: null,
        marker: null,
        circle: null,
      };
    },

    methods: {
      async start() {
        const mapglAPI = await load();
        const apiKey = useRuntimeConfig().public.tGisApiKey;

        this.map = new mapglAPI.Map('2GisMap', {
          center: this.center,
          zoom: this.zoom,
          key: apiKey,
        });

        this.map.on('click', (event) => {
          const clickCoords = event.lngLat;
          this.selectedPoint[0] = clickCoords[0];
          this.selectedPoint[1] = clickCoords[1];
          console.log('Click coords:', clickCoords);

          if (this.marker) {
            this.marker.setCoordinates(clickCoords);
          } else {
            this.marker = new mapglAPI.Marker(this.map, {
              coordinates: clickCoords,
            });
          }

          if (this.enableCircle) {
            // #NOTE - if circle exists, destroy for create new
            if (this.circle) {
              this.circle.destroy();
            }

            this.circle = new mapglAPI.Circle(this.map, {
              coordinates: clickCoords,
              radius: this.radius,
              color: 'rgba(0, 123, 255, 0.3)', // #NOTE - Light blue
              strokeColor: 'rgba(0, 123, 255, 0.6)',
              strokeWidth: 2,
            });
          }
        });
      }
    },

    created() {
      this.start();
    }
  }
</script>
