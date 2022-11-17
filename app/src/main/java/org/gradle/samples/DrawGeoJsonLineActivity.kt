package org.gradle.samples

import android.os.Bundle
import android.view.View
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.mapbox.geojson.Feature
import com.mapbox.geojson.FeatureCollection
import com.mapbox.geojson.LineString
import com.mapbox.geojson.Point
import com.mapbox.maps.CameraOptions
import com.mapbox.maps.MapView
import com.mapbox.maps.Style
import com.mapbox.maps.extension.style.layers.generated.lineLayer
import com.mapbox.maps.extension.style.layers.properties.generated.LineCap
import com.mapbox.maps.extension.style.layers.properties.generated.LineJoin
import com.mapbox.maps.extension.style.sources.generated.geoJsonSource
import com.mapbox.maps.extension.style.style


/**
 * Load a polyline to a style using GeoJsonSource and display it on a map using LineLayer.
 */
//code resource: https://docs.mapbox.com/android/maps/examples/draw-geo-json-line/
class DrawGeoJsonLineActivity : AppCompatActivity() {
    var mapView:MapView?=null
    var showLineBtn:Button?=null
    var sendBtn:Button?=null
    val routeCoordinates=mutableListOf<Point>()

    public override fun onCreate(savedInstanceState:Bundle?){
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_map)
        mapView=findViewById(R.id.mapView)
        showLineBtn=findViewById(R.id.getDataButton)
        sendBtn=findViewById(R.id.sendDataButton)
        showLineBtn?.setVisibility(View.INVISIBLE)
        sendBtn?.setVisibility(View.INVISIBLE)
        initRouteCoordinates()
        mapView?.getMapboxMap()?.setCamera(
            CameraOptions.Builder().center(
                Point.fromLngLat(
                    DrawGeoJsonLineActivity.LATITUDE,
                    DrawGeoJsonLineActivity.LONGITUDE
                )
            ).zoom(DrawGeoJsonLineActivity.ZOOM).build()
        )
        mapView?.getMapboxMap()?.loadStyle(
            (
                    style(styleUri = Style.MAPBOX_STREETS) {
                        +geoJsonSource(DrawGeoJsonLineActivity.GEOJSON_SOURCE_ID) {
                            featureCollection(featureCollection)
                        }
                        +lineLayer("linelayer", DrawGeoJsonLineActivity.GEOJSON_SOURCE_ID) {
                            lineCap(LineCap.ROUND)
                            lineJoin(LineJoin.ROUND)
                            lineOpacity(0.9999)
                            lineWidth(10.0)
                            lineColor("#FF5733")
                        }
                    }
                    )
        )
    }


    var featureLineString = Feature.fromGeometry(LineString.fromLngLats(routeCoordinates))
    var featureCollection = FeatureCollection.fromFeature(featureLineString)


    fun initRouteCoordinates() {
        // Create a list to store our line coordinates.

        routeCoordinates.add(Point.fromLngLat(-1.230805, 52.917281))
        routeCoordinates.add(Point.fromLngLat(-1.230408, 52.917191))
        routeCoordinates.add(Point.fromLngLat(-1.231129, 52.916005))
        routeCoordinates.add(Point.fromLngLat(-1.231455, 52.915496))
        routeCoordinates.add(Point.fromLngLat(-1.231467,  52.915294))

    }

    companion object {
        private const val GEOJSON_SOURCE_ID = "line-source" //before source ID
        private const val LATITUDE = -1.166666
        private const val LONGITUDE = 52.9666628
        private const val ZOOM = 10.0
    }



}
