$(document).ready(function() {
  $('#tree-container').jstree({
    core : {
      data: function(node, callback) {
        var url = "{% url 'locations_api:location-list' %}?parent_key" + (node.id === '#' ? '__isnull=True' : '=' + node.id);
        if ($('#location-type').val()) {
          url += '&location_type_key=' + $('#location-type').val();
        }
        $.ajax({
          url: url
        }).done(function(data) {
          let nodeData = [];
          data.results.forEach(location => {
            location.names.forEach(name => {
              if (name.preferred) {
                nodeData.push({id: location.location_key, text: name.item_name, children: true});
              }
            });

          });
          callback(nodeData);
        });
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

  $('#tree-container')
    // listen for event
    .on('select_node.jstree', function (e, data) {
      $.ajax({
        url: '/locations/' + data.node.id + '/',
        success : function(data) {
          $('#selection-pane').html(data);
          const point = [$('#map-long').val(), $('#map-lat').val()];
          const marker = new ol.Feature(new ol.geom.Point(ol.proj.fromLonLat(point)));
          const view = recorder.map.getView();
          recorder.markerLayer.getSource().addFeature(marker);
          view.setCenter(ol.proj.fromLonLat(point));
          // Set an arbitrary zoom. Would be better if this could be set
          // according to the site boundary.
          view.setZoom(12);
        }
      });
    });

  // Select location type in drop-down filters the locations tree.
  $('#location-type').change(function() {
    $('#tree-container').jstree(true).refresh();
  });

  function initResizableColumns() {
    const GUTTER_SIZE = 6;

    const gutterStyle = dimension => ({
      'flex-basis': `${GUTTER_SIZE}px`,
    });

    const elementStyle = (dimension, size) => ({
      'flex-basis': `calc(${size}% - ${GUTTER_SIZE}px)`,
    })

    // Setup resizeable columns.
    // map.updateSize() is called so that OpenLayers plays nicely on a flex box.
    Split(['#browser-pane', '#detail-pane'], {
      sizes: [33, 67],
      elementStyle: elementStyle,
      gutterStyle: gutterStyle,
      cursor: 'col-resize',
      onDragEnd: function() {
        recorder.map.updateSize();
      }
    });
    recorder.map.updateSize();
  }

  initResizableColumns();
});
