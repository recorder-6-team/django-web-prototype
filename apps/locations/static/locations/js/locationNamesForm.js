$(document).ready(function() {
  $('#add-name').click(function() {
    var formIdx = $('#id_names-TOTAL_FORMS').val();
    $('#location-names_table tbody').append($('tr.empty-form')[0].outerHTML
      .replace(/__prefix__/g, formIdx)
      .replace('d-none empty-form', 'mb-3'));
    $('#id_names-TOTAL_FORMS').val(parseInt(formIdx) + 1);
  });

  // Fake radio behaviour on the preferred name column.
  $('#location-names_table .checkboxinput').click(function() {
    $('#location-names_table .checkboxinput').prop('checked', false);
    $(this).prop('checked', true);
  });
});