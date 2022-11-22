$(document).ready(function() {

  // Section edit button handler.
  $(document).on('click', '.section-edit-btn', {}, function (e) {
    const detailsPane =  $(e.currentTarget).closest('.data-details');
    // Find the item that's currently in view.
    const itemKey = $(detailsPane).data('item-key');
    const entityPath = $(detailsPane).data('entity').replace('_', '-');
    // Find the data section we need to load the form for.
    const section = $(e.currentTarget).data('section');
    $.ajax({
      url: '/places/' + entityPath + '/' + itemKey + '/update/' + section,
      success : function(data) {
        // Add the form to the container.
        $('.panel-cntr-' + section).html(data);
        // Initialise select2 controls.
        $('tr:not(.empty-form) .django-select2:not([data-select2-id])').djangoSelect2({ width: '100%' });
        // Show the collapse container if not already visible.
        $('#collapse-' + section).show();
      }
    });
  });

  $(document).on('click', '.section-form input[type="submit"]', function(e) {
    const sectionForm = $(e.currentTarget).closest('.section-form');
    const section = $(sectionForm).data('section');
    const itemKey = $(e.currentTarget).closest('.data-details').data('item-key');
    const entityPath = $(e.currentTarget).closest('.data-details').data('entity').replace('_', '-');
    let formData = $(sectionForm).serializeArray();
    e.preventDefault();
    // Add the clicked button's value to the form data.
    if (this.value) {
      formData.push({ name: this.name, value: this.value });
    }
    $.ajax({
      type: 'POST',
      // TODO: Make the URL patter DRY using the urlpatterns from the router.
      url: '/places/' + entityPath + '/' + itemKey + '/update/' + section,
      data: formData
    }).done(function(response) {
      $('.panel-cntr-' + section).html(response);
    }).fail(function() {
      // TODO better handling.
      console.log('Form post failed');
    });
  });

  // Add button handler for nested forms.
  $(document).on('click', '.add-form-row', {}, function (e) {
    const section = $(e.currentTarget).data('section');
    const relation = $(e.currentTarget).data('relation');
    const formIdx = $('#id_' + relation  + '-TOTAL_FORMS').val();
    // Copy the empty row form to a new row.
    $('#location-' + section + '_table tbody').append($('#location-' + section + '_table tbody tr.empty-form')[0].outerHTML
      .replace(/__prefix__/g, formIdx)
      .replace('d-none empty-form', 'mb-3'));
    // Increment the row counter.
    $('#id_' + relation + '-TOTAL_FORMS').val(parseInt(formIdx) + 1);
    // Initialise select2 controls.
    $('tr:not(.empty-form) .django-select2:not([data-select2-id])').djangoSelect2({ width: '100%' });
  });

});