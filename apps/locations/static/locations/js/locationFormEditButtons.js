$(document).ready(function() {

  // Section edit button handler.
  $(document).on('click', '.section-edit-btn', {}, function (e) {
    // Find the location that's currently in view.
    const locationKey = $('#location-key').val();
    // Find the data section we need to load the form for.
    const section = $(e.currentTarget).data('section');
    $.ajax({
      url: '/locations/' + locationKey + '/update/' + section,
      success : function(data) {
        // Add the form to the container.
        $('.location-cntr-' + section).html(data);
        // Initialise select2 controls.
        $('.django-select2').not('[data-select2-id]').djangoSelect2({ width: '100%' });
        // Show the collapse container if not already visible.
        $('#collapse-' + section).show();
      }
    });
  });

  // Generic submit button handler.
  function setupFormSubmitButton(section) {
    $(document).on('click', '#location-' + section + '-form input[type="submit"]', function(e) {
      e.preventDefault();
      const locationKey = $('#location-key').val();
      let formData = $('#location-' + section + '-form').serializeArray();
      if (this.value) {
        formData.push({ name: this.name, value: this.value });
      }
      $.ajax({
        type: 'POST',
        url: '/locations/' + locationKey + '/update/' + section,
        data: formData
      }).done(function(response) {
        $('.location-cntr-' + section).html(response);
      }).fail(function() {
        // TODO better handling.
        console.log('Form post failed');
      });
    });
  }

  // Link the submit button handler to the buttons.
  setupFormSubmitButton('names');
  setupFormSubmitButton('general');
  setupFormSubmitButton('designations');
  setupFormSubmitButton('geo-info--admin-areas');
  setupFormSubmitButton('geo-info--land-parcels');
  setupFormSubmitButton('other--relations');
  setupFormSubmitButton('other--uses');
  setupFormSubmitButton('other--approach');

  // Add button handler for nested forms.
  $(document).on('click', '.add-form-row', {}, function (e) {
    let section = $(e.currentTarget).data('section');
    let formIdx = $('#id_' + section + '-TOTAL_FORMS').val();
    // Copy the empty row form to a new row.
    $('#location-' + section + '_table tbody').append($('#location-' + section + '_table tbody tr.empty-form')[0].outerHTML
      .replace(/__prefix__/g, formIdx)
      .replace('d-none empty-form', 'mb-3'));
    // Increment the row counter.
    $('#id_' + section + '-TOTAL_FORMS').val(parseInt(formIdx) + 1);
    // Initialise select2 controls.
    $('.django-select2').not('[data-select2-id]').djangoSelect2({ width: '100%' });
  });

});