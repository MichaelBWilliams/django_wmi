// Style for exposure choropleth
function getColor(d) {
	return 	d > 10.4 ? '#08306b' :
			d > 7.8 ? '#2879b9' :
			d > 5.2 ? '#73b3d8' :
			d > 2.6 ? '#c8ddf0' :
					'#f7fbff';					
};
//function getOpacity(d) {
//	if (d > 0.001) {
//		return .5
//	}
//	else {
//		return .5
//	};
//}

function styleExposure(feature) {
	return {
		fillColor: getColor(feature.properties.percentTotal),
		weight: 0.5,
		opacity: 1, 
		color: '#868686', 
		dasharray: '3',
		fillOpacity: .7
	};
}
// End style for exposure choropleth
