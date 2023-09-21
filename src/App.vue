
<script setup lang="ts">
import { ref } from 'vue'

const message = ref('')
</script>

<template>
  <h1 class="text-5xl m-14 ml-24">Welcome to <span class="font-title text-accent">WordWeaver</span></h1>
  <div class="flex center h-1/2 w-full justify-between items-center flex-col">
    <div class="flex items-end w-4/5">
      <div class="flex flex-col w-full">
        <label for="promptInput" class="text-xl">Enter Your Prompt:</label>
        <input id="promptInput" v-model="message" placeholder="write me a story about..." class="p-4 text-md w-full min-h-[18px]" />
      </div>
      <button class="bg-accent px-10 p-4 h-14 hover:bg-accentDark transition-all">Submit</button>
    </div>
    <div class="w-4/5 h-full p-14 bg-zinc-900 overflow-auto"> {{ message }}</div>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
