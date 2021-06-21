$(document).ready(function() {
  $('#add-name').click(function() {
    var formIdx = $('#id_names-TOTAL_FORMS').val();
    // TODO need an ID on the table to select it accurately.
    $('form table tbody').append($('tr.empty-form')[0].outerHTML
      .replace(/__prefix__/g, formIdx)
      .replace('d-none empty-form', 'mb-3'));
    $('#id_names-TOTAL_FORMS').val(parseInt(formIdx) + 1);
  });

  // Fake radio behaviour on the preferred name column.
  $('table .checkboxinput').click(function() {
    $('table .checkboxinput').prop('checked', false);
    $(this).prop('checked', true);
  });
});