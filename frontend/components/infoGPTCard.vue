<template>
    <v-card class="mx-auto" max-width="600" outlined>
      <v-card-subtitle class="subtitle_text">
        Укажи ваше местоположение и интересуеющее вас расстояние 
      </v-card-subtitle>

      <v-card-text>
        <v-container>
            <v-text-field
                v-model="latitudeInput"
                label="Выбранная Широта"
                outlined
                class="input_field"
                clearable
            ></v-text-field>
        </v-container>
        <v-container>
            <v-text-field
                v-model="longitudeInput"
                label="Выбранная Долгота" 
                outlined
                class="input_field"
                clearable
            ></v-text-field>
        </v-container>
        <v-container>
            <v-text-field
                v-model="radiusInput"
                label="Количество свободных минут"
                outlined
                class="input_field"
                clearable
            ></v-text-field>
        </v-container>
        <v-row class="mt-4 justify-center">
            <v-col cols="auto">
                <!-- Button to fix the place  -->
                <v-btn color="primary" @click="showOnMap" class="show_on_map_btn" variant="outlined" rounded="xl" size="x-large">
                  Зафиксировать местоположения
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
          latitudeInput: 0,
          longitudeInput: 0,
          radiusInput: 0,
          storyText: 'This is where the text will be displayed.'
        }
    },
    methods: {
        tellTheStory() {

        this.storyText = 'Ну а тут дыра в стене, на полу на самом дне. Там есть девочка в стене, на полу на самом дне....'
        // OUTPUT OF GPT API GOES HERE!
        },

        showOnMap() {
            // if(this.longitudeInput===0 && this.latitudeInput===0){
                        
                this.longitudeInput = this.point[0]
                this.latitudeInput = this.point[1]
            // }else{
            // this.point[0]=this.longitudeInput,
            // this.point[1]=this.latitudeInput
            // }
        }
        // showOnMap() {
        // this.$emit('coordinates-updated', {
        //     latitude: this.latitudeInput,
        //     longitude: this.longitudeInput,
        //     radius: this.radiusInput
        // });
        // },
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
  