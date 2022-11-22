$(document).ready(function() {
  $('#tree-container').jstree({
    core : {
      data: function(node, callback) {
        var locationsUrl = "{% url 'places_api:location-list' %}?parent_key" + (node.id === '#' ? '__isnull=True' : '=' + node.id.split(':')[1]);
        var featuresUrl = "{% url 'places_api:location-feature-list' %}?location_key=" + node.id.split(':')[1];
        if ($('#location-type').val()) {
          locationsUrl += '&location_type_key=' + $('#location-type').val();
        }
        $.ajax({
          url: locationsUrl
        }).done(function(data) {
          let nodeData = [];
          data.results.forEach(location => {
            location.names.forEach(name => {
              if (name.preferred) {
                nodeData.push({id: 'location:' + location.location_key, text: name.item_name, children: true});
              }
            });

          });
          callback(nodeData);
        });
        if (node.id !== '#') {
          $.ajax({
            url: featuresUrl
          }).done(function(data) {
            let nodeData = [];
            data.results.forEach(feature => {
              nodeData.push({id: 'location_feature:' + feature.location_feature_key, text: feature.item_name, children: false});

            });
            callback(nodeData);
          });
        }
      },
    },
    types : {
      'default' : {
          'icon' : 'far fa-folder'
      },
      'open' : {
          'icon' : 'far fa-folder-open'
      },
      'closed' : {
          'icon' : 'far fa-folder'
      }
    },
    "plugins" : [ "types" ]
  });

  /**
   * Show a lat long point as a marker on the map.
   *
   * @param array point
   *   X, y coordinate array in GPS lat long.
   */
  function showMapMarker(point) {
    const marker = new ol.Feature(new ol.geom.Point(ol.proj.fromLonLat(point)));
    const view = recorder.map.getView();
    recorder.markerLayer.getSource().addFeature(marker);
    view.setCenter(ol.proj.fromLonLat(point));
    // Set an arbitrary zoom. Would be better if this could be set
    // according to the site boundary.
    view.setZoom(12);
  }

  $('#tree-container')
    // listen for event
    .on('select_node.jstree', function (e, data) {
      // Node ID is table:key format.
      const tokens = data.node.id.split(':');
      const key = tokens[1];
      switch(tokens[0]) {
        case 'location':
          $.ajax({
            url: "{% url 'places:view--locations' 'key_arg' %}".replace('key_arg', key),
            success : function(data) {
              $('#selection-pane').html(data);
              showMapMarker([$('#map-long').val(), $('#map-lat').val()]);
            }
          });
          break;

        case 'location_feature':
          $.ajax({
            url: "{% url 'places:view--location-features' 'key_arg' %}".replace('key_arg', key),
            success : function(data) {
              $('#selection-pane').html(data);
              showMapMarker([$('#map-long').val(), $('#map-lat').val()]);
            }
          });
      }
    });

  // Select location type in drop-down filters the locations tree.
  $('#location-type').change(function() {
    $('#tree-container').jstree(true).refresh();
  });

});
