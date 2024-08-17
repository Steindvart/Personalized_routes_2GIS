<template>
  <div class="preferences-group-container">
    <h1>Постоянные предпочтения</h1>
    <p class="description mt-3">
      ✅ В каждой категории выбери то, что тебе обычно больше нравится. Это будут твои "постоянные предпочтения", которые будут учитываться при каждой генерации маршрута путешествия.
    </p>
    <p class="description mt-3">
      😉 Но, не переживай, ты их можешь изменить в любой момент.
    </p>
    <v-row>
      <v-col>
        <preferences-section
          title="Еда"
          :items="foodItems"
          v-model="selectedFood"
        />
        <preferences-section
          title="Кухня"
          :items="foodStyleItems"
          v-model="selectedFoodStyle"
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
      </v-col>
      <v-col>
        <preferences-section
          title="Места, которые нравятся - Еда"
          :items="placesFoodItems"
          v-model="selectedStyle"
        />

        <preferences-section
          title="Места, которые нравятся - Прогулки"
          :items="placesWalkItems"
          v-model="selectedPlacesWalk"
        />
        <preferences-section
          title="Места, которые нравятся - Развлечения"
          :items="placesFunnItems"
          v-model="selectedPlacesFunn"
        />
      </v-col>
    </v-row>


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
      ],

      foodStyleItems: [
        { text: "Европейская кухня", value: 1 },
        { text: "Азиатская кухня", value: 2 },
      ],

      walkItems: [
        { text: "Парки", value: 1 },
        { text: "Достопримечательности", value: 2 },
        { text: "Архитектура", value: 3 },
      ],

      funItems: [
        { text: "Антикафе", value: 1 },
        { text: "Бар", value: 2 },
        { text: "Караоке", value: 3 },
      ],

      styleItems: [
        { text: "Шумный", value: 1 },
        { text: "Спокойный", value: 2 },
        { text: "Для компании", value: 3 },
        { text: "Одному", value: 4 },
      ],

      placesFoodItems: [
        { text: "Вилка Ложка", value: 1 },
        { text: "Шашлыкoff", value: 2 },
        { text: "Хан Буз", value: 3 },
      ],

      placesWalkItems: [
        { text: "Михайловская набережная", value: 1 },
        { text: "Заельцовский парк", value: 2 },
        { text: "Театр оперы и балета", value: 3 },
      ],

      placesFunnItems: [
        { text: "Друзья", value: 1 },
        { text: "FILET #мяsObar ", value: 3 },
        { text: "21 этаж", value: 4 },
      ],

      selectedFood: [],
      selectedFoodStyle: [],
      selectedWalk: [],
      selectedFunn: [],
      selectedStyle: [],
      selectedPlacesFood: [],
      selectedPlacesFoodStyle: [],
      selectedPlacesWalk: [],
      selectedPlacesFunn: [],
    };
  },

  async created() {
    await this.fetchPreferences();
  },

  methods: {
    async fetchPreferences() {
      try {
        const response = await axios.get("http://localhost:8000/api/preferences/simple");
        const { preferences } = response.data;

        this.selectedFood = this.foodItems.filter(item => preferences.food.includes(item.text));
        this.selectedFoodStyle = this.foodStyleItems.filter(item => preferences.foodStyle.includes(item.text));
        this.selectedWalk = this.walkItems.filter(item => preferences.walk.includes(item.text));
        this.selectedFunn = this.funItems.filter(item => preferences.fun.includes(item.text));
        this.selectedStyle = this.styleItems.filter(item => preferences.style.includes(item.text));

      } catch (error) {
        console.error("Error fetching preferences:", error);
      }
    },

    goToRouteGenerator() {
      this.savePreferences();
      this.$router.push('/generator');
    },

    async savePreferences() {
      const preferences = {
        food: this.selectedFood.map(item => item.text),
        foodStyle: this.selectedFoodStyle.map(item => item.text),
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

<style scoped>
.description {
  font-size: 1rem;
  line-height: 1.5;
  color: #383838;
  font-family: 'Roboto', sans-serif;
  max-width: 800px;
}
</style>
