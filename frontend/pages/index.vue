<template>
  <v-container>
    <h1>Умные путешествия</h1>
    <br/>
    <div>
      <route-settings-card></route-settings-card>
    </div>
    <br/>
  </v-container>
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
