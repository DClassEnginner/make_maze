<template>
  <div class="flex-grow">
    <MazeForm class="border-b-1 border-gray-700" />
    <MazeArea />
    <Ranking />
  </div>
</template>

<script lang="ts">
import MazeForm from "../components/maze/MazeForm.vue";
import MazeArea from "../components/maze/MazeArea.vue";
import Ranking from "../components/maze/Ranking.vue";

export default {
  components: {
    MazeForm,
    MazeArea,
    Ranking
  },
};
</script>
