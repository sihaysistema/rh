<template>
  <div class="mb-4">
    <h4 class="font-weight-bold">{{ counter }}. {{ __(question.text) }}</h4>

    <!-- SI la pregunta es de `key` POSITIVA -->
    <div class="positive_keys mb-2" v-if="question.key === 'POS'">
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
          :value="option"
          v-model="selected"
          @change="emitirEvento"
        />
        <label
          class="custom-control-label"
          :for="[question.name + '-' + option.value]"
        >
          {{ __(option.text) }}</label
        >
      </div>
    </div>

    <!-- SI la pregunta es de `key` NEGATIVA -->
    <div class="positive_keys mb-2" v-if="question.key === 'NEG'">
      <div
        class="custom-control custom-radio"
        v-for="option in negative_keys"
        :key="option.text"
      >
        <input
          type="radio"
          :id="[question.name + '-' + option.value]"
          :name="[question.name + '-' + option.value]"
          class="custom-control-input"
          :value="option"
          v-model="selected"
          @change="emitirEvento"
        />
        <label
          class="custom-control-label"
          :for="[question.name + '-' + option.value]"
        >
          {{ __(option.text) }}</label
        >
      </div>
    </div>

    <span class="mb-3">Eligió: {{ selected }}</span>
  </div>
</template>

<script>
export default {
  props: ["counter", "question"],
  data() {
    return {
      selected: "",
      valueForCalculations: {},
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
    // Emite evento al componente padre, pasando el dato seleccionado
    emitirEvento() {
      this.valueForCalculations = {
        category: this.question.category,
        value: this.selected.value,
        name: this.question.name,
      };

      this.$emit("selected", this.valueForCalculations);
      //   console.log("Usar: ", JSON.stringify(this.valueForCalculations));
    },
  },
};
</script>

<style scoped>
</style>