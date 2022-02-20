import { createStore } from "vuex";

export default createStore({
  state: {
    maze: [[]],
  },
  getters: {
    maze(state) {
      return state.maze;
    },
  },
  mutations: {
    setMaze(state, payload) {
      state.maze = payload.maze;
    },
  },
  actions: {
    updateMaze({ commit }, message) {
      commit("setMaze", { maze: message });
    },
  },
  modules: {},
});
