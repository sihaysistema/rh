<template>
  <div>
    <h4 class="font-weight-bold">{{ question.text }}</h4>

    <div
      class="custom-control custom-radio"
      v-for="option in positive_keys"
      :key="option.text"
    >
      <input
        type="radio"
        :id="[question.name + '-' + option.value]"
        :name="[question.name + '-' + option.value]"
        class="custom-control-input"
        :value="option.text"
        v-model="selected"
        @change="emitirEvento"
      />
      <label
        class="custom-control-label"
        :for="[question.name + '-' + option.value]"
        >{{ option.text }}</label
      >
    </div>
    <br />
    <span>Eligió: {{ selected }}</span>
    <br />
    <br />
  </div>
</template>

<script>
export default {
  props: ["question"],
  data() {
    return {
      selected: "",
      positive_keys: [
        { text: "Very Inaccurate", value: 1 },
        { text: "Moderately Inaccurate", value: 2 },
        { text: "Neither Inaccurate nor Accurate", value: 3 },
        { text: "Moderately Accurate", value: 4 },
        { text: "Very Accurate", value: 5 },
      ],
      negative_keys: [
        { text: "Very Inaccurate", value: 5 },
        { text: "Moderately Inaccurate", value: 4 },
        { text: "Neither Inaccurate nor Accurate", value: 3 },
        { text: "Moderately Accurate", value: 2 },
        { text: "Very Accurate", value: 1 },
      ],
    };
  },
  methods: {
    emitirEvento() {
      this.$emit("selected", this.selected);
    },
  },
};
</script>

<style scoped>
</style>