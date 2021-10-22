<template>
  <div>
    <div class="progress mb-4 Const" style="height: 25px">
      <div
        class="progress-bar"
        role="progressbar"
        :style="progressForm"
        :aria-valuenow="counter"
        aria-valuemin="0"
        aria-valuemax="100"
      >
        60%
      </div>
    </div>

    <div>
      <code>{{ counter }}</code>
      <Question
        v-for="(question, index) in questions"
        :key="question.name"
        :question="question"
        :counter="index + 1"
        @selected="optSelected($event)"
      />

      <button type="button" class="btn btn-dark mb-4" @click="complete_test()">
        {{ __("COMPLETAR") }}
      </button>
    </div>

    <div id="chart"></div>
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
      counter: 0,
      questions: [],
      responseByCategory: [],
      EXTRAVERSION: [],
      AGREEABLENESS: [],
      CONSCIENTIOUSNESS: [],
      NEUROTICISM: [],
      OPENNESS: [],
      dd: {
        labels: [
          __("EXTRAVERSION"),
          __("AGREEABLENESS"),
          __("CONSCIENTIOUSNESS"),
          __("NEUROTICISM"),
          __("OPENNESS"),
        ],
        datasets: [{ values: [18, 40, 30, 35, 8] }],
      },
    };
  },
  // Al montarse el componente se obtiene todas las preguntas a mostrar
  mounted() {
    let _this = this;

    frappe.call({
      method: "rh.api.get_questions",
      callback: function (data) {
        _this.questions = data.message;
        // console.log(data.message);
      },
    });

    new frappe.Chart("#chart", {
      data: this.dd,
      type: "bar",
      height: 180,
      colors: ["red"],
    });
  },
  methods: {
    // Emision de eventos: ver componente Question.vue => emitirEvento()
    optSelected(option) {
      console.log("Seleccionó: ", JSON.stringify(option));
      if (option.category === "EXTRAVERSION") {
        console.log("ES EXTRAVERSION");
        // Si el elemento ya existe en el array, se elimina y se vuelve a agregar
        let index = this.EXTRAVERSION.findIndex((x) => x.name === option.name);

        // Si el valor ya existe en el array, se elimina para volverlo a agregarlo
        // asi asegurar que los calculos se generen correctamente
        if (index >= 0) {
          console.log("Ya existe");
          this.EXTRAVERSION.splice(index, 1);
          this.EXTRAVERSION.push(option);
        } else {
          // Si no existe se agrega
          console.log("No existe");
          this.EXTRAVERSION.push(option);
          this.counter++;
        }
      }

      if (option.category === "AGREEABLENESS") {
        console.log("ES AGREEABLENESS");

        // Si el elemento ya existe en el array, se elimina y se vuelve a agregar
        let index = this.AGREEABLENESS.findIndex((x) => x.name === option.name);

        // Si el valor ya existe en el array, se elimina para volverlo a agregarlo
        // asi asegurar que los calculos se generen correctamente
        if (index >= 0) {
          console.log("Ya existe");
          this.AGREEABLENESS.splice(index, 1);
          this.AGREEABLENESS.push(option);
        } else {
          // Si no existe se agrega
          console.log("No existe");
          this.AGREEABLENESS.push(option);
          this.counter++;
        }
      }

      if (option.category === "CONSCIENTIOUSNESS") {
        console.log("ES CONSCIENTIOUSNESS");

        // Si el elemento ya existe en el array, se elimina y se vuelve a agregar
        let index = this.CONSCIENTIOUSNESS.findIndex(
          (x) => x.name === option.name
        );

        // Si el valor ya existe en el array, se elimina para volverlo a agregarlo
        // asi asegurar que los calculos se generen correctamente
        if (index >= 0) {
          console.log("Ya existe");
          this.CONSCIENTIOUSNESS.splice(index, 1);
          this.CONSCIENTIOUSNESS.push(option);
        } else {
          // Si no existe se agrega
          console.log("No existe");
          this.CONSCIENTIOUSNESS.push(option);
          this.counter++;
        }
      }

      if (option.category === "NEUROTICISM") {
        console.log("ES NEUROTICISM");

        // Si el elemento ya existe en el array, se elimina y se vuelve a agregar
        let index = this.NEUROTICISM.findIndex((x) => x.name === option.name);

        // Si el valor ya existe en el array, se elimina para volverlo a agregarlo
        // asi asegurar que los calculos se generen correctamente
        if (index >= 0) {
          console.log("Ya existe");
          this.NEUROTICISM.splice(index, 1);
          this.NEUROTICISM.push(option);
        } else {
          // Si no existe se agrega
          console.log("No existe");
          this.NEUROTICISM.push(option);
          this.counter++;
        }
      }

      if (option.category === "OPENNESS") {
        console.log("ES OPENNESS");

        // Si el elemento ya existe en el array, se elimina y se vuelve a agregar
        let index = this.OPENNESS.findIndex((x) => x.name === option.name);

        // Si el valor ya existe en el array, se elimina para volverlo a agregarlo
        // asi asegurar que los calculos se generen correctamente
        if (index >= 0) {
          console.log("Ya existe");
          this.OPENNESS.splice(index, 1);
          this.OPENNESS.push(option);
        } else {
          // Si no existe se agrega
          console.log("No existe");
          this.OPENNESS.push(option);
          this.counter++;
        }
      }
    },
    // Valida la existencia de X clave en un array de objectos
    verifyExistence(arrayToVerify, name) {
      return arrayToVerify.some(function (el) {
        return el.name === name; // true/false
      });
    },
    complete_test() {
      let _this = this;

      frappe.call({
        method: "rh.api.complete_test",
        args: {
          data: {
            extraversion: this.EXTRAVERSION,
            agreeableness: this.AGREEABLENESS,
            conscientiousness: this.CONSCIENTIOUSNESS,
            neuroticism: this.NEUROTICISM,
            openness: this.OPENNESS,
          },
        },
        callback: function (data) {
          //   _this.questions = data.message;
          // console.log(data.message);
        },
      });
    },
    contar() {
      console.log("Presiono");
    },
  },
  computed: {
    progressForm: function () {
      return `width: ${this.counter}%`;
    },
  },
};
</script>

<style scoped>
</style>