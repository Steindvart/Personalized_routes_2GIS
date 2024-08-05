<template>
  <div>
    <t-gis-map
      :center="[82.89785, 54.98021]"
      :marker="[82.89785, 54.98021]"
      :styles="{width: '800px', height: '600px'}"
      :zoom="12"
    ></t-gis-map>
  </div>
</template>

<script>
  import tGisMap from '@/components/tGisMap'

  export default {
    name: 'mapPage',
    components: {
      tGisMap
    }
  }
</script>
