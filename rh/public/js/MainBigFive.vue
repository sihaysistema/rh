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
    <code>{{ EXTRAVERSION }}</code>
    <code>{{ AGREEABLENESS }}</code>
    <code>{{ CONSCIENTIOUSNESS }}</code>
    <code>{{ NEUROTICISM }}</code>
    <code>{{ OPENNESS }}</code>
    <!-- Probar emitir eventos -->
    <Question
      v-for="(question, index) in questions"
      :key="question.name"
      :question="question"
      :counter="index + 1"
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
      counter: 0,
      questions: [],
      responseByCategory: [],
      EXTRAVERSION: [],
      AGREEABLENESS: [],
      CONSCIENTIOUSNESS: [],
      NEUROTICISM: [],
      OPENNESS: [],
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
        }
      }
    },
    // Valida la existencia de X clave en un array de objectos
    verifyExistence(arrayToVerify, name) {
      return arrayToVerify.some(function (el) {
        return el.name === name; // true/false
      });
    },
  },
};
</script>

<style scoped>
</style>