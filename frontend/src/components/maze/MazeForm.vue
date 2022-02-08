<template>
  <div>
    <select v-model="selected">
      <option v-for="mt in mazeType" :value="mt.value" :key="mt.id">
        {{ mt.text }}
      </option>
    </select>
    <select v-model="width">
      <option v-for="(width, index) in size" :value="width" :key="index">
        {{ width }}
      </option>
    </select>
    <select v-model="height">
      <option v-for="(height, index) in size" :value="height" :key="index">
        {{ height }}
      </option>
    </select>
    <button @click="readMaze">生成</button>
    <br />
  </div>
</template>

<script lang="ts">
import axios from "axios";

export default {
  data() {
    return {
      selected: {},
      mazeType: [
        { id: 1, text: "棒倒し法", value: "bar" },
        { id: 2, text: "壁伸ばし法", value: "extend" },
        { id: 3, text: "穴掘り法", value: "dig" },
      ],
      size: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
      width: 5,
      height: 5,
    };
  },
  methods: {
    readMaze() {
      console.log((this as any).selected);
      const url =
        "http://localhost:8000/maze/?width=" +
        (this as any).width +
        "&height=" +
        (this as any).height +
        "&type=" +
        (this as any).selected;

      axios.get(url).then(this.response);
      // .then(function (response) {
      //   console.log(response)
      // //   return response.json()
      // // }).then(function(maze) {
      // //   console.log(response)
      // //   this.$store.state.maze = maze['maze']
      // })
    },
    response(response: any) {
      (this as any).$store.state.maze = response.data.maze;
    },
  },
};
</script>
