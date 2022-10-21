$(document).ready(function() {
  $(document).on('click', '#location-add-name', {}, function (e) {
    var formIdx = $('#id_names-TOTAL_FORMS').val();
    $('#location-names_table tbody').append($('tr.empty-form')[0].outerHTML
      .replace(/__prefix__/g, formIdx)
      .replace('d-none empty-form', 'mb-3'));
    $('#id_names-TOTAL_FORMS').val(parseInt(formIdx) + 1);
  });

  // Fake radio behaviour on the preferred name column.
  // TODO find a better way than td:nth-child(2) to select preferred column checkboxes.
  $(document).on('click', '#location-names_table td:nth-child(2) .checkboxinput', {}, function (e) {
    $('#location-names_table td:nth-child(2) .checkboxinput').prop('checked', false);
    $(this).prop('checked', true);
    // Undelete it.
    $(this).closest('tr').find('td:nth-child(4) .checkboxinput').prop('checked', false);
  });

  // Block delete of preferred name row.
  $(document).on('click', '#location-names_table td:nth-child(4) .checkboxinput', {}, function (e) {
    if ($(this).closest('tr').find('td:nth-child(2) .checkboxinput').prop('checked')) {
      $(this).prop('checked', false)
    }
  });
});