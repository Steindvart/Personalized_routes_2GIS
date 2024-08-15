<template>
  <div class="preferences-group-container">
    <h1>Постоянные предпочтения</h1>
    <preferences-section
      title="Еда"
      :items="foodItems"
      v-model="selectedFood"
    />
    <preferences-section
      title="Прогулки"
      :items="walkItems"
      v-model="selectedWalk"
    />
    <preferences-section
      title="Развлечения"
      :items="funItems"
      v-model="selectedFunn"
    />
    <preferences-section
      title="Стиль"
      :items="styleItems"
      v-model="selectedStyle"
    />

    <br />
    <v-btn
      color="primary"
      @click="savePreferences"
      class="save-btn mr-2"
      variant="outlined"
      rounded="xl"
      size="large"
    >
      Сохранить
    </v-btn>
    <v-btn
      color="green"
      class="save-btn"
      variant="outlined"
      rounded="xl"
      size="large"
      large
      @click="goToRouteGenerator"
    >
      Настроить маршрут
    </v-btn>
  </div>
</template>

<script>
import preferencesSection from "@/components/preferencesSection";
import axios from "axios";

export default {
  components: {
    preferencesSection,
  },

  data() {
    return {
      foodItems: [
        { text: "Кафе", value: 1 },
        { text: "Рестораны", value: 2 },
        { text: "Фаст-фуд", value: 3 },
        { text: "Европейская кухня", value: 4 },
        { text: "Азиатская кухня", value: 5 },
      ],

      walkItems: [
        { text: "Парки", value: 1 },
        { text: "Достопримечательности", value: 2 },
        { text: "Архитектура", value: 3 },
      ],

      funItems: [
        { text: "Антикафе", value: 1 },
        { text: "Бар", value: 2 },
        { text: "Клуб", value: 3 },
        { text: "Кальян", value: 4 },
        { text: "Караоке", value: 5 },
        { text: "Игры/Видеоигры", value: 6 },
      ],

      styleItems: [
        { text: "Шумный", value: 1 },
        { text: "Спокойный", value: 2 },
        { text: "Для компании", value: 3 },
        { text: "Одному", value: 4 },
      ],

      selectedFood: [],
      selectedWalk: [],
      selectedFunn: [],
      selectedStyle: [],
    };
  },

  methods: {
    goToRouteGenerator() {
      this.savePreferences();
      this.$router.push('/generator');
    },
    async savePreferences() {
      const preferences = {
        food: this.selectedFood.map(item => item.text),
        walk: this.selectedWalk.map(item => item.text),
        fun: this.selectedFunn.map(item => item.text),
        style: this.selectedStyle.map(item => item.text),
      };

      try {
        const response = await axios.post(
          "http://localhost:8000/api/preferences/simple",
          preferences
        );
        console.log("Preferences saved successfully:", response.data);
      } catch (error) {
        console.error("Error saving preferences:", error);
      }
    },
  },
};
</script>
