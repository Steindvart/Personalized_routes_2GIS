<template>
  <div>
    <h1>Умные путешествия</h1>
    <div>
      <route-settings-card></route-settings-card>
    </div>
  </div>
</template>

<script>
import routeSettingsCard from '@/components/routeSettingsCard'

export default {
  name: 'indexPage',
  components: {
    routeSettingsCard
  },
}
</script>

<style scoped>

</style>
