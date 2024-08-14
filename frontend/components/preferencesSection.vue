<template>
  <v-card class="mx-auto" variant="flat">
    <v-card-text>
      <h2 class="text-h5 mb-2">{{ title }}</h2>
      <v-chip-group
        v-model="localSelectedItems"
        column
        multiple
      >
        <v-chip
          v-for="(item, index) in items"
          :key="index"
          :value="item"
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
  props: {
    title: {
      type: String,
      default: ''
    },
    items: {
      type: Array,
      default: () => []
    },
    modelValue: {
      type: Array,
      default: () => []
    }
  },
  computed: {
    localSelectedItems: {
      get() {
        return this.modelValue;
      },
      set(value) {
        this.$emit('update:modelValue', value);
      }
    }
  }
}
</script>
