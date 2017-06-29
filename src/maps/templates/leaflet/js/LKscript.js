// Set the bounds
var bounds = [
	[10.16,82.75],
	[5.81, 78.36]
];

// initialize the map
var map = L.map('map', {
	center: [7.99, 80.55],
	zoom: 8,
	minZoom: 8,
	maxBounds: bounds, 
	trackResize: true, 
	zoomControl: false
});

// load basemaps
var OSM_hydda = L.tileLayer('http://{s}.tile.openstreetmap.se/hydda/base/{z}/{x}/{y}.png', {
	maxZoom: 18,
	attribution: 'Tiles courtesy of <a href="http://openstreetmap.se/" target="_blank">OpenStreetMap Sweden</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
var OpenMapSurfer_Roads = L.tileLayer('http://korona.geog.uni-heidelberg.de/tiles/roads/x={x}&y={y}&z={z}', {
	maxZoom: 20,
	attribution: 'Imagery from <a href="http://giscience.uni-hd.de/">GIScience Research Group @ University of Heidelberg</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
});
var g_roads = L.gridLayer.googleMutant({
    type: 'roadmap' // valid values are 'roadmap', 'satellite', 'terrain' and 'hybrid'
});
var g_terrain = L.gridLayer.googleMutant({
    type: 'terrain' // valid values are 'roadmap', 'satellite', 'terrain' and 'hybrid'
});
var g_satellite = L.gridLayer.googleMutant({
    type: 'hybrid' // valid values are 'roadmap', 'satellite', 'terrain' and 'hybrid'
});

// Mini map plugin
var osmUrl = 'http://{s}.tile.openstreetmap.se/hydda/base/{z}/{x}/{y}.png';
var osmAttrib = 'Map data &copy; OpenStreetMap contributors';
var osm2 = new L.TileLayer(osmUrl, {attribution: osmAttrib });
var adm1Mini = L.geoJSON(LK_adm1, {
	style: adm1Style
});
var layers = new L.LayerGroup([osm2, adm1Mini]);
var miniMap = new L.Control.MiniMap(layers, {toggleDisplay: true, zoomLevelFixed: 5, centerFixed: [7.99, 80.55]}).addTo(map);
// End mini map plugin

// Zoom home control for plugin
var zoomHome = L.Control.zoomHome();
zoomHome.addTo(map);
// End zoom home control for plugin

// adm 1 layer interaction
function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0
    });
    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}
function clickFeature(e) {
    var layer = e.target;

	infoBase.update(layer.feature.properties);
	map.fitBounds(e.target.getBounds());
}
function resetHighlight(e) {
    adm1Layer.resetStyle(e.target);
}
function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: clickFeature
    });
}


// Exposure layer interaction
function highlightFeature2(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 3,
        color: '#b7b7b7',
        dashArray: '',
        fillOpacity: .8
    });
    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
	infoExposure.update(layer.feature.properties);
}
function clickFeature2(e) {
    var layer = e.target;
//	infoBase.update(layer.feature.properties);
	map.fitBounds(e.target.getBounds());
}
function resetHighlight2(e) {
    exposureLayer.resetStyle(e.target);
}
function onEachFeature2(feature, layer) {
    layer.on({
        mouseover: highlightFeature2,
        mouseout: resetHighlight2,
        click: clickFeature2
    });
}


// Layers
var adm1Layer = L.geoJSON(LK_adm1, {
	style: adm1Style, 
	onEachFeature: onEachFeature
}).bindTooltip(function(layer){return String('<b>' + layer.feature.properties.name + '</b>')}, {direction: "center", className: "admLabel"});


var exposureLayer = L.geoJSON(LK_adm1, {
	style: styleExposure, 
	onEachFeature: onEachFeature2
}).bindTooltip(function(layer){return String('<b>' + layer.feature.properties.name + ': ' + (layer.feature.properties.percentTotal) + '% Exposure' + '</b>')}, {direction: "center", className: "admLabel"});


var branchLayer = L.geoJSON(branchList, {
	
}).bindPopup(function(layer){return String(layer.feature.properties.name)}, {direction: "center", className: "admLabel"});

// Layer groups using styledLayerControl plugin
var baseMaps = [
	{
		groupName: "Base Maps",
		expanded: false,
		layers: {
			"Base Map (Default)": OSM_hydda, 
			"Roads": OpenMapSurfer_Roads, 
			"Google Maps - Roads": g_roads,
			"Google Maps - Terrain": g_terrain,
			"Google Maps - Satellite": g_satellite
		}
	}
];
var overlays = [
	{
		groupName: "Admin 1 Data", 
		expanded: true,
		exclusive: false,
		layers: {
			"Admin 1 Base": adm1Layer, 
			"Admin 1 Exposure": exposureLayer
		}
	}, {
		groupName: "Branch and Point Data", 
		expanded: true, 
		layers: {
			"Branch Points": branchLayer 
		}
	}
];

adm1Layer.StyledLayerControl = {
	removable: false,
	visable: true
};
var options = {
	container_width 	: "300px",
	container_maxHeight : "350px", 
	group_maxHeight     : "300px"
};
var control = L.Control.styledLayerControl(baseMaps, overlays, options);
map.addControl(control);

map.addLayer(adm1Layer);


// Info panel for base layer
var infoBase = L.control();
infoBase.onAdd = function (map) {
	this._div = L.DomUtil.create('div', 'info');
	this.update();
	return this._div;
};
infoBase.update = function (props) {
	this._div.innerHTML = '<h4>Selected Administrative Unit</h4>' + (props ? 'Name: ' + '<b>' + props.name + '</b><br/>' + 'GID # ' + '<b>' + props.gid + '</b><br/>' + 'Maps Available:': 'Click to see:<br/><b>Administrative unit name<br/>GID #<br/>Maps available for download</b>');
};
infoBase.addTo(map);


// info panel control for base layer
map.on('overlayadd', function (eventLayer) {
	if (eventLayer.name === "Admin 1 Base"){
		console.log("boop");
		infoBase.addTo(this);
	} 
//	else {
//		this.removeControl(infoBase);
//	}
});
map.on('overlayadd', function(eventLayer) {
	if (eventLayer.name === "Admin 1 Exposure"){
		infoBase.remove(this);
	}
})


// info panel for exposure layer
var infoExposure = L.control();
infoExposure.onAdd = function (map) {
	this._div = L.DomUtil.create('div', 'info');
	this.update();
	return this._div;
};
function format2(n, currency) {
    return currency + "" + n.toFixed(0).replace(/(\d)(?=(\d{3})+$)/g, "$1,");
}
infoExposure.update = function (props) {
	this._div.innerHTML = '<h4>Selected Administrative Unit</h4>' + (props ? 'Name: ' + '<b>' + props.name + '</b><br/>' + 'GID # ' + '<b>' + props.gid + '</b><br/>' + 'Estimated % of<br/>Total Exposure: ' + '<b>' + props.percentTotal + '%</b><br/>' + '2015 Exposure<br/>in USD: ' + '<b>' + (format2(props.ExposureUSD, "$")) + '</b>' : 'Hover to see:<br/><b>Administrative unit name<br/>GID #<br/>Estimated exposure values</b>');
};
map.on('overlayadd', function (eventLayer) {
	if (eventLayer.name === "Admin 1 Exposure"){
		console.log("boop2");
		infoExposure.addTo(this);
	} 
//	else {
//		this.removeControl(infoExposure);
//	}
});
map.on('overlayadd', function(eventLayer) {
	if (eventLayer.name === "Admin 1 Base"){
		infoExposure.remove(this);
	}
})


// Legend for exposure choropleth
var legendExposure = L.control({position: 'bottomright'});
	legendExposure.onAdd = function (map) {
		var div = L.DomUtil.create('div', 'info legend'),
			grades = [0, 2.6, 5.2, 7.8, 10.4],
			labels = ['<strong> Estimated Percent of<br>Portfolio Exposure </strong>'],
			from, to;
//		If there are admin units with NO exposure, include this style
//		labels.push('<i class="colorcircle" style="background: #888"></i> ' + 'No Exposure');

		for (var i = 0; i < grades.length; i++) {
			from = grades[i];
			to = grades[i + 1];

			labels.push(
				'<i style="background:' + getColor(from + '1' ) + '"></i> ' + from + (to ? '% &ndash; ' + to + '%': '%+' ));
		}
		
		div.innerHTML = labels.join('<br>');
		return div;
	};
map.on('overlayadd', function (eventLayer) {
	if (eventLayer.name === "Admin 1 Exposure"){
//		console.log("boop2");
		legendExposure.addTo(this);
	} 
//	else {
//		this.removeControl(legendExposure);
//	}
});
map.on('overlayremove', function(eventLayer) {
	if (eventLayer.name === "Admin 1 Exposure"){
		legendExposure.remove(this);
	}
})

//make Admin 1 layers mutually exclusive
//the setTimeout is needed to keep the 'overlayadd' event from firing multiple times
map.on('overlayadd', function(eo) {
  if (eo.name === 'Admin 1 Base') {
    setTimeout(function() {
      map.removeLayer(exposureLayer)
    }, 10);
  } else if (eo.name === 'Admin 1 Exposure') {
    setTimeout(function() {
      map.removeLayer(adm1Layer)
    }, 10);
  }
});


// Scale bar plugin
L.control.scale().addTo(map);
// listen for screen resize events
window.addEventListener('resize', function(event){
    // get the width of the screen after the resize event
    var width = document.documentElement.clientWidth;
    // tablets are between 768 and 922 pixels wide
    // phones are less than 768 pixels wide
    if (width < 768) {
        // set the zoom level to 7
        map.setZoom(7);
    }  else {
        // set the zoom level to 8
        map.setZoom(8);
    }
});