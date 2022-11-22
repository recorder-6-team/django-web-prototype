$(document).ready(function($) {
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
})