
<script setup lang="ts">
import { ref } from 'vue'
import { useFetch } from '@vueuse/core'

import {ArrowPathIcon} from '@heroicons/vue/24/solid';

const message = ref('')
const SERVER_ENDPOINT = ref('http://192.168.2.33:5000/hello')

const {data, isFetching, error} = useFetch(SERVER_ENDPOINT, {refetch:true}).get().text()

const loadingText = '....'

const generateData = async() => {
  data.value = ''
  SERVER_ENDPOINT.value='http://192.168.2.33:5000/cohere-generate/' + message.value
  console.log(SERVER_ENDPOINT.value);
  
}

if (error.value) {
  alert('Error getting data')
}

</script>

<template>
  <h1 class="text-5xl m-14 ml-24">Welcome to <span class="font-title text-accent">WordWeaver</span></h1>
  <div class="flex center h-1/2 w-full justify-between items-center flex-col">
    <div class="flex items-end w-4/5">
      <div class="flex flex-col w-full">
        <label for="promptInput" class="text-xl">Enter Your Prompt:</label>
        <input id="promptInput" v-model="message" placeholder="write me a story about..." class="p-4 text-md w-full min-h-[18px]" />
      </div>
      <button class="bg-accent px-10 p-4 h-14 hover:bg-accentDark transition-all" @click="generateData"> <ArrowPathIcon v-if="isFetching" class="animate-spin h-full w-full fill-white"/> <span v-if="!isFetching">Submit</span></button>
    </div>
    
    <div class="w-4/5 h-full p-14 bg-zinc-900 overflow-auto"> <span class="" v-if="isFetching || data==''">{{loadingText}}</span>{{ data }} </div>
  </div>
</template>
