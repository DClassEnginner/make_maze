<template>
  <div class="pt-2 pl-2 pr-2 w-2/3 sm:w-2/4 mx-auto">
    <form
      class="bg-white shadow-md rounded-t px-8 pt-6 pb-8 border-b-2 border-gray-200"
    >
      <div class="mb-4">
        <label
          class="text-gray-700 float-left block md:flex md:py-2 md:px-3 text-base font-bold mb-2"
          >生成タイプ</label
        >
        <select
          class="shadow border rounded md:flex md:mt-0 md:mr-0 md:mb-0 md:ml-auto w-full md:w-2/4 py-2 px-3 text-gray-700 leading-tight"
          v-model="selected.value"
        >
          <option v-for="mt in mazeType" :value="mt.value" :key="mt.id">
            {{ mt.text }}
          </option>
        </select>
      </div>
      <div class="mb-4">
        <label
          class="text-gray-700 float-left block md:flex md:py-2 md:px-3 text-base font-bold mb-2"
          >迷路のサイズ</label
        >
        <select
          class="shadow border rounded md:flex md:mt-0 md:mr-0 md:mb-0 md:ml-auto w-full md:w-2/4 py-2 px-3 text-gray-700 leading-tight"
          v-model="size"
        >
          <option v-for="(size, index) in sizeList" :value="size" :key="index">
            {{ size }}
          </option>
        </select>
      </div>
      <div class="items-center justify-between">
        <button
          type="button"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-3"
          @click="readMaze"
        >
          生成
        </button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      selected: { id: 1, text: "棒倒し法", value: "bar" },
      mazeType: [
        { id: 1, text: "棒倒し法", value: "bar" },
        // { id: 2, text: "壁伸ばし法", value: "extend" },
        // { id: 3, text: "穴掘り法", value: "dig" },
      ],
      sizeList: [5, 10, 15, 20, 25],
      size: 5,
    };
  },
  methods: {
    readMaze() {
      const url =
        "http://localhost:8000/maze/?width=" +
        (this as any).size +
        "&height=" +
        (this as any).size +
        "&type=" +
        (this as any).selected.value;
      
      console.log(url);

      axios.get(url).then(this.setMaze);
      // .then(function (response) {
      //   console.log(response)
      // //   return response.json()
      // // }).then(function(maze) {
      // //   console.log(response)
      // //   this.$store.state.maze = maze['maze']
      // })
    },

    setMaze(res: any) {
      (this as any).$store.dispatch("updateMaze", res.data.maze);
    },
  },
});
</script>
