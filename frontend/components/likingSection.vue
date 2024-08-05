<template>
  <v-card class="mx-auto">
    <v-card-text>
      <h2 class="text-h5 mb-2">{{ title }}</h2>

      <v-chip-group
        v-model="selectedItems"
        column
        multiple
      >
        <v-chip
          v-for="(item, index) in items"
          :key="index"
          :text="item.text"
          :value="item.value"
          variant="outlined"
          filter
        >
          {{ item.text }}
        </v-chip>
      </v-chip-group>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      selectedItems: [],
    };
  },

  props: {
    title: {
      type: String,
      default: ''
    },
    items: {
      type: Array,
      default: () => []
    }
  }
}
</script>
