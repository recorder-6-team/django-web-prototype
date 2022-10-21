$(document).ready(function() {
  $(document).on('click', '.section-edit-btn', {}, function (e) {
    // Find the location that's currently in view.
    const locationKey = $('#location-key').val();
    // Find the data section we need to load the form for.
    const section = $(e.currentTarget).data('section');
    $.ajax({
      url: '/locations/' + locationKey + '/update/' + section,
      success : function(data) {
        $('.location-cntr-' + section).html(data)
      }
    });
  });

  function setupFormSubmitButton(section) {
    $(document).on('submit', '#location-' + section + '-form', function(e) {
      e.preventDefault();
      const locationKey = $('#location-key').val();
      // Clone the form into a data array to post.
      var data = {'action': 'post'};
      $.each($('#location-' + section + '-form :input[name!=""][name]'), function() {
        data[$(this).attr('name')] = $(this).val();
      });
      $.ajax({
        type: 'POST',
        url: '/locations/' + locationKey + '/update/' + section,
        data: $('#location-' + section + '-form').serialize()
      }).done(function(response) {
        $('.location-cntr-' + section).html(response)
      }).fail(function() {
        // TODO better handling.
        console.log('Form post failed');
      });
    });
  }

  setupFormSubmitButton('names');
  setupFormSubmitButton('general');
  setupFormSubmitButton('designations');
  setupFormSubmitButton('other-approach');

});