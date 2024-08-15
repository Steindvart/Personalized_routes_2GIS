<template>
  <v-card class="mx-auto" max-width="600" subtitle="Места, которые подходят под ваши активности и предпочтения" outlined>
    <template v-slot:title>
      <span class="font-weight-black">Маршрут путешествия</span>
    </template>
    <v-card-text>
      <v-timeline density="compact" side="end" align="start">
        <v-timeline-item
          v-for="(item, i) in items"
          :key="i"
          :dot-color="item.color"
          :icon="item.icon"
          fill-dot
          size="large"
        >
          <v-card>
            <v-card-title :class="['text-h6', `bg-${item.color}`]">
              {{ item.name }}
            </v-card-title>
            <v-card-text class="bg-white text--primary limited-width" v-if="item.desc.length != 0">
              <p>{{ item.desc }}</p>
            </v-card-text>
          </v-card>
        </v-timeline-item>
      </v-timeline>

      <!-- Кнопка "Начать путешествие" по центру внизу элементов -->
      <div class="start-journey-container">
        <v-btn color="teal" @click="startJourney" class="start-journey-btn" variant="outlined" rounded="xl" size="large">
          Перенастроить маршрут
        </v-btn>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      default: () => [0, 0],
    }
  },
}
</script>

<style scoped>
.limited-width {
  max-width: 400px; /* Устанавливаем максимальную ширину для текста */
  margin: 0 auto; /* Центрируем текст */
}

</style>
