<template>
  <v-card class="mx-auto" max-width="600" subtitle="Укажи активности, средний чек и другие текущие предпочтения" outlined>
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
      <v-btn @click="addActivity" class="add-activity-btn" outlined :disabled="activities.length >= 4">
        Добавить активность
      </v-btn>

      <!-- Средний чек -->
      <v-select
        v-model="averageCheck"
        :items="averageCheckOptions"
        label="Максимальный средний чек"
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

      <!-- Способ передвижения -->
      <v-select
        v-model="wayType"
        :items="wayTypeOptions"
        label="Способ передвижения"
        prepend-icon="mdi-road"
        class="mt-3"
      ></v-select>

      <!-- Хочу чего-то нового -->
      <v-switch
        v-model="wantSomethingNew"
        label="Хочу чего-то нового"
        inset
        color="primary"
      ></v-switch>

      <!-- Сообщение об ошибке -->
      <v-alert
        v-if="error"
        type="error"
        dismissible
        v-model="error"
        class="mt-3"
      >
        {{ errorMessage }}
      </v-alert>

      <!-- Кнопка "Начать путешествие" по центру внизу элементов -->
      <div class="start-journey-container">
        <v-btn color="primary" @click="startJourney" class="start-journey-btn" variant="outlined" rounded="xl" size="x-large" block>
          Начать путешествие
        </v-btn>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  props: {
    point: {
      type: Array,
      default: () => [0, 0],
    },
  },

  data() {
    return {
      activities: ['Поесть'],
      activityOptions: ['Поесть', 'Погулять', 'Развлечься', 'Шопинг'],
      averageCheck: 1500,
      averageCheckOptions: [500, 1000, 1500, 2000, 3000],
      totalTime: '2 часа',
      totalTimeOptions: ['1 час', '2 часа', '3 часа', '4 часа', 'Более 4 часов'],
      wayType: 'Пешком',
      wayTypeOptions: ['Пешком', 'Автомобиль', 'Общественный транспорт'],
      wantSomethingNew: false,
      error: false,
      errorMessage: ''
    }
  },

  methods: {
    addActivity() {
      if (this.activities.length < 4) {
        this.activities.push('')
      }
    },
    removeActivity(index) {
      if (this.activities.length > 1) {
        this.activities.splice(index, 1)
      }
    },
    async startJourney() {
      // Проверка, была ли выбрана начальная точка
      if (this.point[0] === 0 && this.point[1] === 0) {
        this.error = true
        this.errorMessage = 'Пожалуйста, выберите начальную точку на карте перед началом путешествия.'
        return
      } else {
        this.error = false
      }

      let totalTimeMinutes = 60

      if (this.totalTime == '2 часа') totalTimeMinutes = totalTimeMinutes * 2
      else if (this.totalTime == '3 часа') totalTimeMinutes = totalTimeMinutes * 3
      else if (this.totalTime == '4 часа') totalTimeMinutes = totalTimeMinutes * 4
      else if (this.totalTime == 'Более 4 часов') totalTimeMinutes = totalTimeMinutes * 6

      const routePreferences = {
        activities: this.activities,
        averageCheck: this.averageCheck,
        totalTime: totalTimeMinutes,
        wantSomethingNew: this.wantSomethingNew,
        wayType: this.wayType,
        point: {
          lon: this.point[0],
          lat: this.point[1],
        },
      }

      try {
        // Отправка данных на сервер
        const response = await axios.post('http://localhost:8000/api/generate-journey', routePreferences)
        console.info(response.data)
        const routeData = response.data.data.places

        // Сохранение данных в localStorage
        console.info(routeData)
        localStorage.setItem('routeData', JSON.stringify(routeData));

        // Переход на страницу journey
        this.$router.push({ name: 'journey' });
      } catch (error) {
        console.error('Ошибка при генерации маршрута:', error)
      }
    },
  },
}
</script>



<style scoped>
.activity-number {
  width: 20px;
  text-align: right;
  margin-right: 10px;
}

.add-activity-btn {
  width: calc(100% - 120px);
  margin-top: -10px;
  margin-left: 65px;
  text-transform: none;
}

.start-journey-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.start-journey-btn {
  text-transform: none;
}

.v-card {
  position: relative;
}
</style>
