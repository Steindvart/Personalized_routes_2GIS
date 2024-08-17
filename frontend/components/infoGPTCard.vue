<template>
    <v-card class="mx-auto" max-width="600" >
    <p class="subtitle_text">
      🤖Привет! Я молодой, но очень активный виртуальный гид! 
    </p>
      <p class="subtitle_text">
        
        😎Я с радостью поведает вам об интересных местах поблизости.  
        (Я еще учусь - по этому могу ошибаться в предоставляемых данных.😇👉👈)
      </p>

      <v-card-text>
      <!--<v-card-subtitle class="subtitle_text">
        Укажи ваше местоположение и интересуеющее вас расстояние 
      </v-card-subtitle>
         <v-container>
          <p class="input_field">Широта: {{ point[0] }}</p><p class="input_field"> Долгота: {{point[1] }}</p>
            <v-text-field
                v-model="localradius"
                label="Радиус поиска"
                outlined
                class="input_field"
                clearable
            ></v-text-field>
        </v-container> 
        <v-row class="mt-4 justify-center">
            <v-col cols="auto">
                <v-btn color="primary" @click="fixRadius" class="show_on_map_btn" variant="outlined" rounded="xl" size="x-large">
                  Зафиксировать радиус
                </v-btn>
            </v-col>
        </v-row>-->
        <v-container >
            <v-row class="justify-center">
                <v-col cols="auto" >
                    <!-- Button to find get info from GPT -->
                    <v-btn color="green" @click="tellTheStory" class="tell_the_story_btn" variant="outlined" rounded="xl" size="x-large">
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
import { Text } from 'vue';
  
  
    export default {
      props: {
        point: {
          type: Array,
          default: () => [0, 0],
        },
        radius: {
          type: Number,
        }
      },

    data() {
        return {
          localradius: this.radius,
          storyText: 'This is where the text will be displayed.'
        }
    },

    methods: {
        tellTheStory() {

        this.storyText = 'Ну а тут дыра в стене, на полу на самом дне. Там есть девочка в стене, на полу на самом дне....'
        // OUTPUT OF GPT API GOES HERE!
        },



        fixRadius() {
        if(this.point[0] !==0 && this.point[1] !==0){
          this.$emit('radius-updated', {
            radius: localradius
        })
        }
      },
  },
  }
  </script>
  
  <style scoped>
  .show_on_map_btn {
    text-transform: none;
  }
  .tell_the_story_btn {
    text-transform: none;
  }
  .subtitle_text {
  word-wrap: break-word;
  white-space: normal;
  font-size: 1rem;
  line-height: 1.5;
  color: #383838;
  font-family: 'Roboto', sans-serif;
  max-width: 1000px;
  padding: 5px;

  }
  .input_field {
    font-size: 16px;
    height: 40px; 
  }
  
  .story_text{
    font-size: 16px; /* Customize font size */
    padding: 5px;
    /* border: 1px solid #ccc;*/
    background-color: #f9f9f931;
  }
  </style>
  