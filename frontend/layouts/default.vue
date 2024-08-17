<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer
        expand-on-hover
        rail
        floating
        permanent
      >
        <v-list>
          <v-list-item
            prepend-avatar="https://randomuser.me/api/portraits/women/45.jpg"
            subtitle="maria_i92@yandex.ru"
            title="Мария Иванова"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <nuxt-link to="/" exact class="custom-link">
            <v-list-item prepend-icon="mdi-home" title="Главная"></v-list-item>
          </nuxt-link>
          <nuxt-link to="/generator" exact class="custom-link">
            <v-list-item prepend-icon="mdi-map" title="Начать путешествие"></v-list-item>
          </nuxt-link>
          <nuxt-link to="/preferences" exact class="custom-link">
            <v-list-item prepend-icon="mdi-star" title="Предпочтения"></v-list-item>
          </nuxt-link>
          <nuxt-link to="/guide" exact class="custom-link">
            <v-list-item prepend-icon="mdi-brain" title="GPT-гайд"></v-list-item>
          </nuxt-link>
          <nuxt-link to="/map" exact class="custom-link">
            <v-list-item prepend-icon="mdi-map" title="Карта"></v-list-item>
          </nuxt-link>
        </v-list>
      </v-navigation-drawer>
       <v-main>
        <v-container>
          <slot></slot>
        </v-container>
      </v-main>
    </v-layout>
  </v-card>
</template>

<style scoped>
.custom-link {
  text-decoration: none;
  color: inherit;
}

.custom-link:hover {
  text-decoration: none;
}
</style>