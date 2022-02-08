<template>
  <div id="app">
    <Header />
    <Sidebar />
    <Maze />
    <Footer />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Header from "./components/modules/Header.vue";
import Sidebar from "./components/modules/Sidebar.vue";
import Maze from "./views/Maze.vue";
import Footer from "./components/modules/Footer.vue";

export default defineComponent({
  components: {
    Header,
    Sidebar,
    Maze,
    Footer,
  },
});
</script>
