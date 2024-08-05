<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer
        expand-on-hover
        rail
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
          <v-list-item prepend-icon="mdi-home" title="Главная" value="myfiles"></v-list-item>
          <v-list-item prepend-icon="mdi-map" title="Карта" value="shared"></v-list-item>
          <v-list-item prepend-icon="mdi-star" title="Избранное" value="starred"></v-list-item>
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