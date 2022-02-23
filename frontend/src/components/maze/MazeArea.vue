<template>
  <div class="pr-6 pl-6 pb-2 sm:px-2 w-full sm:w-3/4 md:w-2/4 mx-auto h-full mb-4">
    <div class="bg-white shadow-md rounded-b px-8 pt-6 pb-8 mb-4 min-h-full">
      <table v-if="maze.length > 0" class="m-auto">
        <tr v-for="(mz, index) in maze" :key="index">
          <!-- <td v-for="(m, index) in mz" :key="index" :class="{ 'wall' : m==1, 'path': m==0 }"> -->
          <td v-for="(m, index) in mz" :key="index" class="w-4 h-4 table-cell" :class="classObject(m)">
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  computed: {
    maze() {
      return this.$store.getters.maze;
    }
  },
  methods: {
    classObject(m: number) {
      return {
        'bg-black': m == 1,
        'bg-white': m == 0
      }
    },
  },
});
</script>
