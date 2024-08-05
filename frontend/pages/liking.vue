<template>
  <div class="liking-group-container">
    <h1>Постоянные предпочтения</h1>
    <liking-section
      title="Категории"
      :items=categoryItems
    >
    </liking-section>
    <br/>
    <liking-section
      title="Стиль"
      :items=styleItems
    >
    </liking-section>
  </div>
</template>

<script>
import likingSection from "@/components/likingSection";

export default {
  components: {
    likingSection,
  },
  data() {
    return {
      categoryItems: [
        { text: 'Кафе', value: 1 },
        { text: 'Рестораны', value: 2 },
        { text: 'Парки', value: 3 },
        { text: 'Достопримечательности', value: 4 },
        { text: 'Красота', value: 5 },
        { text: 'Развлечения', value: 6 },
        { text: 'Шопинг', value: 7 },
        { text: 'Анти-кафе', value: 8 },
      ],

      styleItems: [
        { text: 'Детский', value: 1 },
        { text: 'Взрослый', value: 2 },
        { text: 'Шумный', value: 3 },
        { text: 'Спокойный', value: 4 },
        { text: 'Для компании', value: 5 },
        { text: 'Одному', value: 6 },
      ],
    };
  },
}
</script>