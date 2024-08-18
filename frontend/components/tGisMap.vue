<template>
  <div id="2GisMap" :style="styles" class="map"></div>
</template>

<script>
import { load } from '@2gis/mapgl';
import { Directions } from '@2gis/mapgl-directions';

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
    enableMarker: {
      type: Boolean,
      default: true
    },
    enableCircle: {
      type: Boolean,
      default: false
    },
    selectedPoint: {
      type: Array,
      default: () => [0, 0],
    },
    routePoints: {
      type: Array,
      default: () => [],
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
      directions: null
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

      if (this.routePoints.length > 1) {
        console.info(this.routePoints)
        this.directions = new Directions(this.map, {
          directionsApiKey: apiKey,
        });

        console.info('points')
        console.info(this.routePoints)

        this.directions.pedestrianRoute({
          points: this.routePoints,
          style: {
            routeLineWidth: [
                'interpolate',
                ['linear'],
                ['zoom'],
                10,
                20, // Ширина основной линии будет меняться от 30 пикселей на масштабе 10 и ниже...
                14,
                3, // ...до 3 пикселей на масштабе 14 и выше
            ],
          },
        });
      }

      this.map.on('click', (event) => {
        const clickCoords = event.lngLat;
        this.selectedPoint[0] = clickCoords[0];
        this.selectedPoint[1] = clickCoords[1];
        console.log('Click coords:', clickCoords);

        if (this.enableMarker) {
          if (this.marker) {
            this.marker.setCoordinates(clickCoords);
          } else {
            this.marker = new mapglAPI.Marker(this.map, {
              coordinates: clickCoords,
            });
          }
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

<style scoped>
.map {
  width: 100%;
  height: 100%;
}
</style>