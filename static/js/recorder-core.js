window.recorder = {
  data: {},
  fns: {}
};
/*
Context data for the page can be injected as a json object in the recorder-data element.
See html.html template.
*/
var dataEl = document.getElementById('recorder-data');
if (dataEl) {
  window.recorder.data = JSON.parse(dataEl.textContent);
}