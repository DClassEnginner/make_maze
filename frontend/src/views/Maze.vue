<template>
  <div>
    <MazeForm />
    <MazeArea />
  </div>
</template>

<script lang="ts">
import MazeForm from "../components/maze/MazeForm.vue";
import MazeArea from "../components/maze/MazeArea.vue";

export default {
  components: {
    MazeForm,
    MazeArea,
  },
};
</script>
