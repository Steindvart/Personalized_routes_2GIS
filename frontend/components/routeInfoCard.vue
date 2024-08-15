<template>
  <v-card class="mx-auto" max-width="600" subtitle="Места, которые подходят под ваши активности и предпочтения" outlined>
    <template v-slot:title>
      <span class="font-weight-black">Маршрут путешествия</span>
    </template>
    <v-card-text>
      <v-timeline density="compact" side="end" align="start">
        <v-timeline-item
          v-for="(item, i) in itemsWithIconsAndColors"
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
            <v-card-text v-if="item.desc" class="bg-white text--primary limited-width">
              <p class="description">{{ item.desc }}</p>
              <v-chip v-if="item.rating"
                append-icon="mdi-star"
                class="mt-2"
                color="orange"
              >
                {{ item.rating }}
              </v-chip>
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
      required: true,
    },
  },
  computed: {
    itemsWithIconsAndColors() {
      return this.items.map(item => {
        let icon = '';
        let color = '';

        switch (item.type) {
          case 'start':
            icon = 'mdi-flag-checkered';
            color = 'blue';
            break;
          case 'food':
            icon = 'mdi-coffee';
            color = 'red-lighten-2';
            break;
          case 'walk':
            icon = 'mdi-walk';
            color = 'green-lighten-1';
            break;
          case 'fun':
            icon = 'mdi-party-popper';
            color = 'purple-lighten-2';
            break;
          default:
            icon = 'mdi-help-circle';
            color = 'grey';
        }

        return {
          ...item,
          icon,
          color,
        };
      });
    },
  },
  methods: {
    startJourney() {
      console.log("Перенастройка маршрута", this.items);
    },
  },
}
</script>

<style scoped>
.limited-width {
  max-width: 400px;
  font-family: 'Roboto', sans-serif;
}

.description {
  margin-top: 8px;
  font-size: 14px;
  line-height: 1.3;
}

</style>
