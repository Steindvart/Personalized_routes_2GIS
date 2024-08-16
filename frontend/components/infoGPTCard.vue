<template>
    <v-card class="mx-auto" max-width="600" outlined>
      <v-card-subtitle class="subtitle_text">
        Укажи ваше местоположение и удобный вам радиус поиска
      </v-card-subtitle>

      <v-card-text>
        <v-container>
            <v-text-field
                v-model="latitudeInput"
                label="Широта"
                outlined
                class="input_field"
                clearable
            ></v-text-field>
        </v-container>
        <v-container>
            <v-text-field
                v-model="longitudeInput"
                label="Долгота"
                outlined
                class="input_field"
                clearable
            ></v-text-field>
        </v-container>
        <v-container>
            <v-text-field
                v-model="radiusInput"
                label="Радиус поиска"
                outlined
                class="input_field"
                clearable
            ></v-text-field>
        </v-container>
        <v-row class="mt-4 justify-center">
            <v-col cols="auto">
                <!-- Button to find the place in map -->
                <v-btn color="primary" @click="addActivity" class="show_in_map_btn" variant="outlined" rounded="xl" size="x-large">
                Покажи на карте
                </v-btn>
            </v-col>
        </v-row>
        <v-container >
            <v-row class="justify-center">
                <v-col cols="auto" >
                    <!-- Button to find get info from GPT -->
                    <v-btn color="primary" @click="tellTheStory" class="tell_the_story_btn" variant="outlined" rounded="xl" size="x-large">
                    Расскажи историю
                    </v-btn>
                </v-col>
            </v-row>
            <div class="story_text">{{ storyText }}</div>
        </v-container>

  
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
          latitudeInput: '',
          longitudeInput: '',
          radiusInput: '',
          storyText: 'This is where the text will be displayed.'
        }
    },
    methods: {
        tellTheStory() {
        this.storyText = 'The story!'
        }
    },







  }
  </script>
  
  <style scoped>
  .activity-number {
    width: 20px;
    text-align: right;
    margin-right: 10px;
  }
  
  .start-journey-container {
    display: flex;
    justify-content: center;
    margin-top: 20px;
  }
  
  .v-card {
    position: relative;
  }








  .show_in_map_btn {
    text-transform: none;
  }
  .tell_the_story_btn {
    text-transform: none;
  }
  .subtitle_text {
  word-wrap: break-word;
  white-space: normal;
  }
  .input_field {
  height: 20px; 
  }
  .story_text{
    font-size: 16px; /* Customize font size */
    padding: 5px;
    /* border: 1px solid #ccc;*/
    background-color: #f9f9f931;
  }



  </style>
  