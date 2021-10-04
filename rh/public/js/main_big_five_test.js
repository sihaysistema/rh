frappe.provide('frappe.rh');   // create a namespace within the Frappe instance

import MainBigFive from './MainBigFive.vue';

frappe.rh.BigFiveTest = class {   // create a glue class, wich will manage your Vue instance
  constructor({ parent }) {
    this.$parent = $(parent);
    this.page = parent.page;
    this.setup_header();
    this.make_body();
  }
  make_body() {
    this.$main_big_five_test = this.$parent.find('.layout-main');   // bind the new Vue instance to the main <div> on the page
    this.vue = new Vue({
      el: this.$main_big_five_test[0],
      data: {
        // timer: ''
      },
      render: h => h(MainBigFive),

    });
  }
  setup_header() {
  }
};