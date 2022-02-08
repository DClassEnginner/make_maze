<template>
  <div>
    <span v-for="(mz, index) in maze" :key="index">
      <span v-for="(m, index) in mz" :key="index">
        <span v-if="m == 1">■</span>
        <span v-else>□</span>
      </span>
      <br />
    </span>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  computed: {
    maze() {
      return this.$store.state.maze;
    },
  },
});
</script>
