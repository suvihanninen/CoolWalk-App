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

    public override fun onCreate(savedInstanceState:Bundle?){
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_draw_geo_json_line)
        mapView=findViewById(R.id.mapView)

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
                            featureCollection(PointListSingleton.featureCollection)
                        }
                        +lineLayer("linelayer", DrawGeoJsonLineActivity.GEOJSON_SOURCE_ID) {
                            lineCap(LineCap.ROUND)
                            lineJoin(LineJoin.ROUND)
                            lineOpacity(0.9999)
                            lineWidth(2.0)
                            lineColor("#FF5733")
                        }
                    }
                    )
        )
    }

    companion object {
        private const val GEOJSON_SOURCE_ID = "line-source" //before source ID
        private const val LATITUDE = -1.166666
        private const val LONGITUDE = 52.9666628
        private const val ZOOM = 10.0
    }



}
