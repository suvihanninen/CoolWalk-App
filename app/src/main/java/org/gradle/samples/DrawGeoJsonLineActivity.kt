package org.gradle.samples

import android.os.Bundle
import android.view.View
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
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
    var mapView: MapView? = null
    var button: Button? = null
    public override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_map)
        mapView = findViewById(R.id.mapView)
        button = findViewById(R.id.button)
        button?.setVisibility(View.INVISIBLE)
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
                        url("https://github.itu.dk/krot/CoolWalk/blob/63891fab2657a3c77dc0b3d1e1ab6842415dca5b/app/src/main/res/raw/example.geojson")
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
        /*mapView?.getMapboxMap()?.loadStyleUri(Style.MAPBOX_STREETS, object : Style.OnStyleLoaded {
            override fun onStyleLoaded(style: Style) {

            }})*/




    }

    companion object {
        private const val GEOJSON_SOURCE_ID = "line"
        private const val LATITUDE =  52.9666628
        private const val LONGITUDE =  -1.166666
        private const val ZOOM = 2.0
    }


}
