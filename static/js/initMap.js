{% load static %}

const olConfig = {
  target: 'map',
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM()
    })
  ]
};
var centre;
if (recorder.data.centreMap) {
  centre = [recorder.data.centreMap.lon, recorder.data.centreMap.lat];
  zoom = 9;
}
else {
  centre = [-2, 55];
  zoom = 5;
}

olConfig.view = new ol.View({
  center: ol.proj.fromLonLat(centre),
  zoom: zoom
});
recorder.map = new ol.Map(olConfig);

recorder.markerLayer = new ol.layer.Vector({
  source: new ol.source.Vector(),
  style: new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.5, 1],
      src: "{% static 'img/marker.png' %}"
    })
  })
});
recorder.map.addLayer(recorder.markerLayer);

if (recorder.data.centreMap) {
  const marker = new ol.Feature(new ol.geom.Point(ol.proj.fromLonLat([recorder.data.centreMap.lon, recorder.data.centreMap.lat])));
  recorder.markerLayer.getSource().addFeature(marker);
}