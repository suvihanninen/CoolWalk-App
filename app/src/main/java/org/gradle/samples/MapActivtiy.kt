package org.gradle.samples



//Imports to add annotations
import android.content.Context
import android.content.Intent
import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.drawable.BitmapDrawable
import android.graphics.drawable.Drawable
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.annotation.DrawableRes
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.content.res.AppCompatResources
import com.google.gson.GsonBuilder
import com.mapbox.geojson.Point
import com.mapbox.maps.MapView
import com.mapbox.maps.Style
import com.mapbox.maps.plugin.annotation.annotations
import com.mapbox.maps.plugin.annotation.generated.PointAnnotationOptions
import com.mapbox.maps.plugin.annotation.generated.createPointAnnotationManager
import com.mapbox.maps.plugin.gestures.gestures
import okhttp3.*
import java.io.IOException


class MapActivtiy:AppCompatActivity(){
    var mapView: MapView? = null
    lateinit var showLineBtn: Button
    lateinit var sendBtn: Button
    lateinit var fromLon: TextView
    lateinit var fromLat: TextView
    lateinit var toLat: TextView
    lateinit var toLon: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_map)
        showLineBtn = findViewById(R.id.getDataButton)
        sendBtn = findViewById(R.id.sendDataButton)
        mapView = findViewById(R.id.mapView)
        fromLon = findViewById(R.id.fromLongitude)
        fromLat = findViewById(R.id.fromLatitude)
        toLon = findViewById(R.id.toLongitude)
        toLat = findViewById(R.id.toLatitude)
        var counter=0
        mapView?.getMapboxMap()?.loadStyleUri(Style.MAPBOX_STREETS)

        sendBtn.setOnClickListener {
            fetchGeoJson()
        }


        //Make API call in the fetchGeoJson()

        println("We are should have fetched the JSON now")
        showLineBtn.setOnClickListener {

            val intent = Intent(this, DrawGeoJsonLineActivity::class.java)
            startActivity(intent)
        }

    //Collect lon and lat
        mapView?.gestures?.addOnMapClickListener {
            var latitude = it.latitude()
            var longitude = it.longitude()
            mapView?.getMapboxMap()?.loadStyleUri(Style.MAPBOX_STREETS, object : Style.OnStyleLoaded {
                override fun onStyleLoaded(style: Style) {
                    addAnnotationToMap(latitude, longitude)

                    if(counter==0){
                        fromLon.text = longitude.toString()
                        fromLat.text = latitude.toString()
                    }else if(counter==1){
                        toLon.text = longitude.toString()
                        toLat.text = latitude.toString()
                    }
                    counter++
                }
            })

            true
        }

    }


    private fun addAnnotationToMap(latitude: Double, longitude: Double) {
        // Create an instance of the Annotation API and get the PointAnnotationManager.
        //code resource: https://docs.mapbox.com/android/maps/examples/default-point-annotation/
        println("hellohello")
        //the bellow codeblock is executed only with non-null values --> if bitmapFromDrawableRes != null then execute the let. Gives bitmap as an argument and
        bitmapFromDrawableRes(this@MapActivtiy, R.mipmap.red_marker_foreground)?.let {
            val annotationApi = mapView?.annotations
            val pointAnnotationManager = annotationApi?.createPointAnnotationManager()
            // Set options for the resulting symbol layer.
            val pointAnnotationOptions: PointAnnotationOptions = PointAnnotationOptions()
                // Define a geographic coordinate.
                .withPoint(Point.fromLngLat(longitude, latitude))
                // Specify the bitmap you assigned to the point annotation
                // The bitmap will be added to map style automatically.

                .withIconImage(it)
                // Add the resulting pointAnnotation to the map.
            pointAnnotationManager?.create(pointAnnotationOptions)

        }
    }
    private fun bitmapFromDrawableRes(context: Context, @DrawableRes resourceId: Int): Bitmap?{
        var returnBitmap = convertDrawableToBitmap(AppCompatResources.getDrawable(context, resourceId))

        return returnBitmap

    }


    private fun convertDrawableToBitmap(sourceDrawable: Drawable?): Bitmap? {
        if (sourceDrawable == null) {
            return null
        }

        return if (sourceDrawable is BitmapDrawable) {
            sourceDrawable.bitmap
        } else {
// copying drawable object to not manipulate on the same reference
            val constantState = sourceDrawable.constantState ?: return null
            val drawable = constantState.newDrawable().mutate()
            val bitmap: Bitmap = Bitmap.createBitmap(
                drawable.intrinsicWidth, drawable.intrinsicHeight,
                Bitmap.Config.ARGB_8888
            )
            val canvas = Canvas(bitmap)
            drawable.setBounds(0, 0, canvas.width, canvas.height)
            drawable.draw(canvas)
            bitmap
        }
    }

    fun fetchGeoJson(){
        println("Fetching JSON now")
        //We need an URL to pass it to the Request.Builder
        val url = "http://127.0.0.1:4000/from/${fromLat}/to/${toLat}"

        //Make a okHttp client
        val client = OkHttpClient()

        val request = Request.Builder().url(url)
            .build()

        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {
                println("Request failed ${e.localizedMessage}")
            }

            /**
             * The gson is used to build the JSON
             * Since the data fetching is happening on a background thread we need to call a UI thread
             * to make the data visible on our UI
             */
            override fun onResponse(call: Call, response: Response) {
                //The body is our geoJson file?
                val body = response.body?.string()

                print("This is a body of API request $body")
                val gson = GsonBuilder().create()
                val breedFeed = gson.fromJson(body, FeatureCollection::class.java)
                runOnUiThread {


                }
            }
        })
    }


    data class FeatureCollection (
        val features: List<Feature>,
        val type: String
    )

    data class Feature (
        val geometry: Geometry,
        val properties: Properties,
        val type: String
    )

    data class Geometry (
        val coordinates: List<List<Point>>,
        val type: String
    )

    class Properties()

    override fun onStart()
    {
        super.onStart()
        mapView?.onStart()
    }

    override fun onStop()
    {
        super.onStop()
        mapView?.onStop()
    }

    override fun onLowMemory()
    {
        super.onLowMemory()
        mapView?.onLowMemory()
    }

    override fun onDestroy() {
        super.onDestroy()
        mapView?.onDestroy()
    }


}

