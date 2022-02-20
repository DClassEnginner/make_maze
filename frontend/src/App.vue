<template>
  <div id="main" class="flex flex-col min-h-screen bg-gray-200">
    <Header />
    <Message />
    <Maze />
    <Footer />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Header from "./components/modules/Header.vue";
import Message from "./components/modules/Message.vue";
import Maze from "./views/Maze.vue";
import Footer from "./components/modules/Footer.vue";

export default defineComponent({
  components: {
    Header,
    Message,
    Maze,
    Footer,
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
