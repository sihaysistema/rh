frappe.pages['big-five-test'].on_page_load = function (wrapper) {
  var page = frappe.ui.make_app_page({
    parent: wrapper,
    title: 'Big Five Test',
    single_column: true
  });

  this.page.$main_page_big_five_test = new frappe.rh.BigFiveTest(this.page);
}