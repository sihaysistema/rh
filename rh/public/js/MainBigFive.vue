<template>
  <div>
    <div v-if="completed === false">
      <div class="container">
        <div class="row">
          <div class="col-sm-10 position-fixed">
            <!-- Barra de progreso -->
            <div class="progress mb-4 mt-4" style="height: 20px" v-if="completed === false">
              <div
                class="progress-bar"
                role="progressbar"
                :style="progressForm"
                :aria-valuenow="counter"
                aria-valuemin="0"
                aria-valuemax="100">
                {{ counter }}%
              </div>
            </div>
          </div>
          <!-- DIVISION -->
          <div class="col-sm-8">
            <div class="separacion">
              <!-- Inicio renderizacion de preguntas -->
              <Question
                v-for="(question, index) in questions"
                :key="question.name"
                :question="question"
                :counter="index + 1"
                @selected="optSelected($event)" />

              <button type="button" class="btn btn-dark mb-4" @click="complete_test()">
                {{ __("COMPLETE") }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Seccion Resultados -->
    <div v-if="completed === true" class="mb-4">
      <h3 class="texto-res">{{ __("Results") }}</h3>
      <p class="texto-res">{{ __("Date and Time") }}: {{ dateTimeTest }}</p>
      <p class="texto-res">{{ __("Test Completed By") }}: {{ userTest }}</p>
    </div>

    <!-- Seccion render de grafica con resultados de la prueba -->
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
      dateTimeTest: "",
      userTest: "",
      completed: false,
      counter: 0,
      questions: [],
      responseByCategory: [],
      EXTRAVERSION: [],
      AGREEABLENESS: [],
      CONSCIENTIOUSNESS: [],
      NEUROTICISM: [],
      OPENNESS: [],
      dd: {
        labels: [__("EXTRAVERSION"), __("AGREEABLENESS"), __("CONSCIENTIOUSNESS"), __("NEUROTICISM"), __("OPENNESS")],
        datasets: [{ values: [0, 0, 0, 0, 0] }], // Valores default para graficas
      },
    };
  },
  // Al montarse el componente se obtiene todas las preguntas a mostrar en la prueba
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
    // Segun la opcion que marque el usuario se van a ir agrupando por categoria BIG5
    // Evitando duplicados
    optSelected(option) {
      //   console.log("Seleccionó: ", JSON.stringify(option));
      if (option.category === "EXTRAVERSION") {
        // console.log("ES EXTRAVERSION");
        // Si el elemento ya existe en el array, se elimina y se vuelve a agregar
        let index = this.EXTRAVERSION.findIndex((x) => x.name === option.name);

        // Si el valor ya existe en el array, se elimina para volverlo a agregarlo
        // asi asegurar que los calculos se generen correctamente
        if (index >= 0) {
          //   console.log("Ya existe");
          this.EXTRAVERSION.splice(index, 1);
          this.EXTRAVERSION.push(option);
        } else {
          // Si no existe se agrega
          //   console.log("No existe");
          this.EXTRAVERSION.push(option);
          this.counter++;
        }
      }

      if (option.category === "AGREEABLENESS") {
        // console.log("ES AGREEABLENESS");

        // Si el elemento ya existe en el array, se elimina y se vuelve a agregar
        let index = this.AGREEABLENESS.findIndex((x) => x.name === option.name);

        // Si el valor ya existe en el array, se elimina para volverlo a agregarlo
        // asi asegurar que los calculos se generen correctamente
        if (index >= 0) {
          //   console.log("Ya existe");
          this.AGREEABLENESS.splice(index, 1);
          this.AGREEABLENESS.push(option);
        } else {
          // Si no existe se agrega
          //   console.log("No existe");
          this.AGREEABLENESS.push(option);
          this.counter++;
        }
      }

      if (option.category === "CONSCIENTIOUSNESS") {
        // console.log("ES CONSCIENTIOUSNESS");

        // Si el elemento ya existe en el array, se elimina y se vuelve a agregar
        let index = this.CONSCIENTIOUSNESS.findIndex((x) => x.name === option.name);

        // Si el valor ya existe en el array, se elimina para volverlo a agregarlo
        // asi asegurar que los calculos se generen correctamente
        if (index >= 0) {
          //   console.log("Ya existe");
          this.CONSCIENTIOUSNESS.splice(index, 1);
          this.CONSCIENTIOUSNESS.push(option);
        } else {
          // Si no existe se agrega
          //   console.log("No existe");
          this.CONSCIENTIOUSNESS.push(option);
          this.counter++;
        }
      }

      if (option.category === "NEUROTICISM") {
        // console.log("ES NEUROTICISM");

        // Si el elemento ya existe en el array, se elimina y se vuelve a agregar
        let index = this.NEUROTICISM.findIndex((x) => x.name === option.name);

        // Si el valor ya existe en el array, se elimina para volverlo a agregarlo
        // asi asegurar que los calculos se generen correctamente
        if (index >= 0) {
          //   console.log("Ya existe");
          this.NEUROTICISM.splice(index, 1);
          this.NEUROTICISM.push(option);
        } else {
          // Si no existe se agrega
          //   console.log("No existe");
          this.NEUROTICISM.push(option);
          this.counter++;
        }
      }

      if (option.category === "OPENNESS") {
        // console.log("ES OPENNESS");

        // Si el elemento ya existe en el array, se elimina y se vuelve a agregar
        let index = this.OPENNESS.findIndex((x) => x.name === option.name);

        // Si el valor ya existe en el array, se elimina para volverlo a agregarlo
        // asi asegurar que los calculos se generen correctamente
        if (index >= 0) {
          //   console.log("Ya existe");
          this.OPENNESS.splice(index, 1);
          this.OPENNESS.push(option);
        } else {
          // Si no existe se agrega
          //   console.log("No existe");
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
    // Se ejecuta al presionar el boton completar, las opciones seleccionadas se mandan al backend
    // para ser validadas, guardadas y comparadas con los perfiles de personalidad adecuados
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
        freeze: true,
        callback: function (r) {
          if (r.message[0]) {
            // Si se completo correctamente
            _this.completed = true; // Para mostrar los resultado

            // Descomentar el console si quiere saber la estrucutura retornada por el server
            _this.dd.datasets[0].values[0] = r.message[1].total_extraversion;
            _this.dd.datasets[0].values[1] = r.message[1].total_agreeableness;
            _this.dd.datasets[0].values[2] = r.message[1].total_conscientiousness;
            _this.dd.datasets[0].values[3] = r.message[1].total_neuroticism;
            _this.dd.datasets[0].values[4] = r.message[1].total_openness;

            _this.dateTimeTest = r.message[1].datetimetest;
            _this.userTest = r.message[1].user;

            _this.$forceUpdate();

            new frappe.Chart("#chart", {
              data: _this.dd,
              type: "bar",
              height: 225,
              animate: 1,
              colors: ["#0069a1"],
            });

            _this.$forceUpdate();
            frappe.utils.play_sound("submit");
          } else {
            _this.completed = false;
            frappe.show_alert(
              {
                indicator: "red",
                message: r.message[1],
              },
              60
            );
          }

          //   console.log(r.message);
        },
      });
    },
  },
  computed: {
    // Clase dinamica para div que refleja el avance del progress bar
    progressForm: function () {
      return `width: ${this.counter}%`;
    },
  },
};
</script>

<style scoped>
.texto-res {
  color: #333c44;
}

.container {
  position: relative;
}

/* Style the header: fixed position (always stay at the top) */
.position-fixed {
  background-color: #f9fafa;
  z-index: 9999;
}

.separacion {
  margin-top: 65px;
}
</style>