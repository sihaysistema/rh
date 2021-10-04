<template>
  <div>
    <div class="progress mb-4" style="height: 25px">
      <div
        class="progress-bar"
        role="progressbar"
        style="width: 25%"
        aria-valuenow="25"
        aria-valuemin="0"
        aria-valuemax="100"
      >
        25%
      </div>
    </div>

    <!-- Probar emitir eventos -->
    <Question
      v-for="question in questions"
      :key="question.name"
      :question="question"
      @selected="optSelected($event)"
    />
  </div>
</template>

<script>
import Question from "./components/Question.vue";
export default {
  name: "MainBigFive",
  components: {
    Question,
  },
  data() {
    return {
      questions: [],
      responseByCategory: [],
    };
  },
  mounted() {
    let _this = this;

    frappe.call({
      method: "rh.api.get_questions",
      callback: function (data) {
        _this.questions = data.message;
        console.log(data.message);
      },
    });
  },
  methods: {
    // Emision de eventos
    optSelected(option) {
      console.log("Seleccionó: ", option);
    },
  },
};
</script>

<style>
</style>