<script setup lang="ts">
import Sidebar from './components/Sidebar.vue'
</script>

<template>
  <div class="flex h-screen w-full bg-gray-50 font-sans">
    <Sidebar />
    <router-view class="flex-1 overflow-y-auto" />
  </div>
</template>