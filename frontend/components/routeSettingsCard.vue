<template>
  <v-card class="mx-auto" max-width="600" subtitle="Укажите активности, средний чек и другие текущие предпочтения" outlined>
    <template v-slot:title>
      <span class="font-weight-black">Настройка маршрута</span>
    </template>
    <v-card-text>
      <!-- Активность -->
      <div v-for="(activity, index) in activities" :key="index" class="mb-3 d-flex align-items-center">
        <span class="activity-number">{{ index + 1 }}.</span>
        <v-select
          v-model="activities[index]"
          :items="activityOptions"
          label="Выберите активность"
          prepend-icon="mdi-run"
          class="flex-grow-1 mr-2"
        ></v-select>
        <v-btn v-if="index > 0" @click="removeActivity(index)" icon small>
          <v-icon>mdi-minus-circle-outline</v-icon>
        </v-btn>
        <div v-else style="width: 48px;"></div> <!-- Пустое пространство для выравнивания первого элемента -->
      </div>

      <!-- Кнопка добавления активности -->
      <v-btn @click="addActivity" class="add-activity-btn" outlined>
        Добавить активность
      </v-btn>

      <!-- Средний чек -->
      <v-select
        v-model="averageCheck"
        :items="averageCheckOptions"
        label="Средний чек"
        prepend-icon="mdi-cash"
        class="mt-10"
      ></v-select>

      <!-- Общее время на маршрут -->
      <v-select
        v-model="totalTime"
        :items="totalTimeOptions"
        label="Общее время на маршрут"
        prepend-icon="mdi-clock-outline"
        class="mt-3"
      ></v-select>

      <!-- Хочу чего-то нового -->
      <v-switch
        v-model="wantSomethingNew"
        label="Хочу чего-то нового"
        inset
      ></v-switch>
    </v-card-text>

    <!-- Кнопка "Начать путешествие" в правом нижнем углу -->
    <v-card-actions class="justify-end">
      <v-btn color="primary" @click="startJourney" class="start-journey-btn" variant="outlined">Начать путешествие</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      activities: ['Поесть'],
      activityOptions: ['Поесть', 'Погулять', 'Выпить', 'Шопинг'],
      averageCheck: null,
      averageCheckOptions: [500, 1000, 1500, 2000, '>2500'],
      totalTime: null,
      totalTimeOptions: ['1 час', '2 часа', '3 часа', '4 часа', 'Более 4 часов'],
      wantSomethingNew: false,
    }
  },
  methods: {
    addActivity() {
      if (this.activities.length < 6) {
        this.activities.push('')
      }
    },
    removeActivity(index) {
      if (this.activities.length > 1) {
        this.activities.splice(index, 1)
      }
    },
    async startJourney() {
      let totalTimeMinutes = 60;

      if (this.totalTime == '2 часа') totalTimeMinutes = totalTimeMinutes * 2;
      else if (this.totalTime == '3 часа') totalTimeMinutes = totalTimeMinutes * 3;
      else if (this.totalTime == '4 часа') totalTimeMinutes = totalTimeMinutes * 4;
      else if (this.totalTime == 'Более 4 часов') totalTimeMinutes = totalTimeMinutes * 6;


      const routePreferences = {
        activities: this.activities,
        averageCheck: this.averageCheck,
        totalTime: totalTimeMinutes,
        wantSomethingNew: this.wantSomethingNew,
      }

      try {
        // Отправка данных на сервер
        // #TODO - make as Vuex with axios base URL
        const response = await axios.post('http://localhost:8000/api/generate-journey', routePreferences)
        console.log('Маршрут сгенерирован:', response.data)
      } catch (error) {
        console.error('Ошибка при генерации маршрута:', error)
      }
    }
  }
}
</script>

<style scoped>
.activity-number {
  width: 20px;
  text-align: right;
  margin-right: 10px;
}

.add-activity-btn {
  width: calc(100% - 120px); /* 100% ширины минус отступы и ширина иконки */
  margin-top: -10px;
  margin-left: 65px;
  text-transform: none;
}

.start-journey-btn {
  position: absolute;
  bottom: 16px;
  right: 16px;
}

.v-card {
  position: relative;
}
</style>
