<template>
  <div
    class="box relative py-2 px-6 sm:px-2 w-full sm:w-3/4 md:w-2/4 mx-auto mb-2"
    v-show="flg"
  >
    <img
      class="relative rounded w-full h-full"
      src="../../../public/static/img/labyrinth.jpg"
      alt="labyrinth"
      title="labyrinth"
      @load="load"
    />
    <div
      className="absolute transform -translate-y-1/2 top-1/2 left-0 right-0 text-center text-white bg-black py-4 mx-6 sm:mx-2 text-xl xl:text-2xl"
    >
      自動生成された迷路をクリアしよう！
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      flg: false,
    };
  },
  methods: {
    load() {
      this.flg = true;
    },
  },
});
</script>
