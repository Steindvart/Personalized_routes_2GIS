<template>
  <v-card class="mx-auto" max-width="600">
    <v-card-text>
      <p class="subtitle_text">
        🤖 Привет! Я твой виртуальный гид и готов рассказать тебе об интересных местах поблизости.
      </p>
      <v-alert
        text="Я еще учусь - поэтому могу ошибаться в предоставляемых данных."
        title="Возможны ошибки!"
        type="warning"
        class="warning_alert"
      ></v-alert>
      <v-row class="justify-center mb-4">
        <v-btn
          color="green"
          @click="fetchStory"
          class="tell_the_story_btn"
          :loading="loading"
          variant="outlined"
          rounded="xl"
          size="large">
          Расскажи историю
        </v-btn>
      </v-row>
      <v-skeleton-loader v-if="loading" class="mt-4" type="article" />
      <div v-else-if="story" class="story_text">
        <v-alert
          color="primary"
          theme="dark"
          prominent
        >
          {{ story }}
        </v-alert>
      </div>
      <div v-else class="story_text">
        <v-alert
          title="История будет здесь, когда ты нажмёшь на кнопку."
          color="primary"
          theme="dark"
          prominent
        >
        </v-alert>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    point: Array,
    radius: Number,
    loading: Boolean,
    story: String,
  },
  methods: {
    fetchStory() {
      this.$emit('fetch-story');
    }
  }
}
</script>

<style scoped>
.tell_the_story_btn {
  text-transform: none;
  margin-top: 16px;
}

.subtitle_text {
  font-size: 1rem;
  line-height: 1.5;
  color: #383838;
  font-family: 'Roboto', sans-serif;
}

.story_text {
  font-size: 16px;
  padding: 5px;
  background-color: #f9f9f9;
  border-radius: 5px;
  color: #424242;
}
.warning_alert{
  margin-bottom: 16px; /* Add margin to create space between the alert and the button */
  z-index: 1; /* Ensure the alert is on top */
}
</style>
