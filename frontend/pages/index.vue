<template>
  <v-container class="full-width-container text-center">
    <v-row class="justify-center align-center" style="height: 100vh;">
      <v-col cols="12" md="8">
        <v-card outlined>
          <v-card-text>
            <h1 class="headline font-weight-bold">Умные путешествия</h1>
            <p class="description">
              Персональные маршруты, созданные на основе ваших постоянных и текущих предпочтений.
              Настройте ваши постоянные предпочтения, чтобы получать персонализированные рекомендации
              и создавайте маршруты, учитывающие ваше настроение и условия в данный момент.
            </p>
            <v-divider class="my-8"></v-divider>
            <v-row justify="center" class="mb-4">
              <v-btn
                color="primary"
                @click="goToPreferences"
                class="mr-4"
                rounded="xl"
                size="large"
                large
              >
                Настроить постоянные предпочтения
              </v-btn>
              <v-btn color="green" @click="goToRouteGenerator" rounded="xl" size="large" large>Настроить маршрут</v-btn>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  methods: {
    goToPreferences() {
      this.$router.push('/preferences');
    },
    goToRouteGenerator() {
      this.$router.push('/generator');
    }
  }
}
</script>

<style scoped>
.full-width-container {
  max-width: 100%;
  padding: 0;
  background-color: #f5f5f5;
}

.headline {
  font-size: 2.3rem;
  color: #424242;
}

.description {
  font-size: 1.1rem;
  line-height: 1.6;
  margin: 20px 0;
  color: #757575;
}

v-divider {
  margin: 20px 0;
}

v-btn {
  font-size: 1rem;
  text-transform: none;
}
</style>
