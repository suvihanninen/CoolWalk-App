package org.gradle.samples



//Imports to add annotations
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.textfield.TextInputEditText
import com.google.android.material.textfield.TextInputLayout
import com.google.gson.GsonBuilder
import com.mapbox.geojson.FeatureCollection
import com.mapbox.geojson.LineString
import com.mapbox.geojson.Point
import com.mapbox.geojson.internal.typeadapters.RuntimeTypeAdapterFactory
import com.mapbox.maps.MapView
import com.mapbox.maps.Style
import okhttp3.*
import org.json.JSONObject
import java.io.IOException


class MapActivtiy:AppCompatActivity() {
    var mapView: MapView? = null
    lateinit var showLineBtn: Button
    lateinit var sendBtn: Button
    lateinit var fromInput: TextInputEditText
    lateinit var toInput: TextInputEditText
    lateinit var fromInputLayout: TextInputLayout



    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_map)
        showLineBtn = findViewById(R.id.getDataButton)
        sendBtn = findViewById(R.id.sendDataButton)
        fromInput = findViewById(R.id.from_Input)
        toInput = findViewById(R.id.to_Input)
        fromInputLayout = findViewById(R.id.fromInputLayout)

        /** Will be used in further implementation
        lateinit var fromLon: Point
        lateinit var fromLat: Point
        lateinit var toLon: Point
        lateinit var toLat: Point
        var counter = 0
         **/


        mapView?.getMapboxMap()?.loadStyleUri(Style.MAPBOX_STREETS)

        sendBtn.setOnClickListener {
            if(fromInput.text.toString()!="" &&  toInput.text.toString()!="") {
               fetchGeoJson(fromInput.text.toString(), toInput.text.toString())
            }else{
                val myToast = Toast.makeText(this, "Please, input from and to nodes.", Toast.LENGTH_LONG)
                myToast.show()
            }
        }

        showLineBtn.setOnClickListener {
            val intent = Intent(this, DrawGeoJsonLineActivity::class.java)
            startActivity(intent)
        }

        /**
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
        }**/


    }


    fun fetchGeoJson(from: String?, to: String?) {
        val fromNode: Int? = from?.toInt()
        val toNode: Int? = to?.toInt()
        println("Fetching JSON now $from and $to")
        //val featureObject = JSONObject("""{"features": [{"geometry": {"coordinates": [[-1.106321, 52.965347], [-1.106523, 52.966218], [-1.106675, 52.966204], [-1.107652, 52.966116], [-1.108331, 52.966054], [-1.108718, 52.966018], [-1.109553, 52.965944], [-1.109235, 52.964633], [-1.109036, 52.963744], [-1.109819, 52.963774], [-1.111205, 52.960773], [-1.111618, 52.959832], [-1.112093, 52.959586], [-1.112754, 52.959541], [-1.111552, 52.958683], [-1.111084, 52.958341], [-1.112433, 52.958242], [-1.112343, 52.957551], [-1.113667, 52.95569], [-1.117185, 52.957306], [-1.11785, 52.956792], [-1.118447, 52.956339], [-1.119196, 52.955868], [-1.120175, 52.955303], [-1.121231, 52.954768], [-1.121475, 52.954637], [-1.121796, 52.954469], [-1.122374, 52.954162], [-1.125264, 52.9559], [-1.127471, 52.954868], [-1.128914, 52.954259], [-1.129449, 52.954516], [-1.130158, 52.954847], [-1.130231, 52.954787], [-1.131038, 52.95323], [-1.131147, 52.952815], [-1.131195, 52.952631], [-1.131234, 52.95244], [-1.131293, 52.952192], [-1.131493, 52.95162], [-1.1321, 52.951886], [-1.132643, 52.950757], [-1.132934, 52.950819], [-1.133441, 52.950927], [-1.1343, 52.951113], [-1.135264, 52.951328], [-1.135515, 52.951375], [-1.135595, 52.951452], [-1.13626, 52.95139], [-1.137817, 52.95131], [-1.138469, 52.951263], [-1.139222, 52.950428], [-1.139419, 52.950414], [-1.140172, 52.950724], [-1.140234, 52.950861], [-1.140515, 52.951483], [-1.142295, 52.951119], [-1.142283, 52.95105], [-1.14376, 52.950882], [-1.145347, 52.951146], [-1.1459, 52.951345], [-1.146234, 52.951404], [-1.145907, 52.952117]], "type": "LineString"}, "properties": {}, "type": "Feature"}], "type": "FeatureCollection"}"""")
        //val featureObject = "{\"features\": [{\"geometry\": {\"coordinates\": [[-1.106321, 52.965347], [-1.106523, 52.966218], [-1.106675, 52.966204], [-1.107652, 52.966116], [-1.108331, 52.966054], [-1.108718, 52.966018], [-1.109553, 52.965944], [-1.109235, 52.964633], [-1.109036, 52.963744], [-1.109819, 52.963774], [-1.111205, 52.960773], [-1.111618, 52.959832], [-1.112093, 52.959586], [-1.112754, 52.959541], [-1.111552, 52.958683], [-1.111084, 52.958341], [-1.112433, 52.958242], [-1.112343, 52.957551], [-1.113667, 52.95569], [-1.117185, 52.957306], [-1.11785, 52.956792], [-1.118447, 52.956339], [-1.119196, 52.955868], [-1.120175, 52.955303], [-1.121231, 52.954768], [-1.121475, 52.954637], [-1.121796, 52.954469], [-1.122374, 52.954162], [-1.125264, 52.9559], [-1.127471, 52.954868], [-1.128914, 52.954259], [-1.129449, 52.954516], [-1.130158, 52.954847], [-1.130231, 52.954787], [-1.131038, 52.95323], [-1.131147, 52.952815], [-1.131195, 52.952631], [-1.131234, 52.95244], [-1.131293, 52.952192], [-1.131493, 52.95162], [-1.1321, 52.951886], [-1.132643, 52.950757], [-1.132934, 52.950819], [-1.133441, 52.950927], [-1.1343, 52.951113], [-1.135264, 52.951328], [-1.135515, 52.951375], [-1.135595, 52.951452], [-1.13626, 52.95139], [-1.137817, 52.95131], [-1.138469, 52.951263], [-1.139222, 52.950428], [-1.139419, 52.950414], [-1.140172, 52.950724], [-1.140234, 52.950861], [-1.140515, 52.951483], [-1.142295, 52.951119], [-1.142283, 52.95105], [-1.14376, 52.950882], [-1.145347, 52.951146], [-1.1459, 52.951345], [-1.146234, 52.951404], [-1.145907, 52.952117]], \"type\": \"LineString\"}, \"properties\": {}, \"type\": \"Feature\"}], \"type\": \"FeatureCollection\"}"




        val url = "http://10.110.61.94:4000/coolwalk?fro=${fromNode}&to=${toNode}"
        //val url1 = "http://127.0.0.1:4000/"

        //Make a okHttp client
        val client = OkHttpClient()

        val request = Request.Builder().url(url).build()

        client.newCall(request).enqueue(object : Callback {

            override fun onFailure(call: Call, e: IOException) {
                println("Request failed ${e.localizedMessage}")
            }

            /**
             * The gson is used to build the JSON
             * Since the data fetching is happening on a background thread we need to call a UI thread
             * to make the data visible on our UI
             */
            override fun onResponse(call: Call, response: okhttp3.Response) {
                //The body is our geoJson file?
                println("Before assigning the body")
                val adapter = RuntimeTypeAdapterFactory
                        .of(Geometry::class.java)
                        .registerSubtype(LineString::class.java)


                val body = response.body?.string()

                print("This is a body of API request $body")
               val gson = GsonBuilder().setPrettyPrinting().registerTypeAdapterFactory(adapter).create()
                //This code will be in the Response callback method once the API is ready.
                //Here featureObject.toString() is equvivalent to the GeoJSON object that we get from the Flask API
                val response = gson.fromJson(body, Response::class.java)
                val coordsList =  response.features[0].geometry.coordinates
                val itr = coordsList.listIterator()
                while (itr.hasNext()) {
                    PointListSingleton.addpoint(itr.next())
                }
                val featureCollection = gson.fromJson(body, FeatureCollection::class.java)
                runOnUiThread {


                }
            }
        })
    }



        data class Response(
            val features: List<Feature>,
            val type: String?
        )

        data class Feature(
            val geometry: Geometry,
            val properties: Properties,
            val type: String?
        )

        data class Geometry(
            val coordinates: List<List<Double>>,
            val type: String?
        )

        class Properties()

        override fun onStart() {
            super.onStart()
            mapView?.onStart()
        }

        override fun onStop() {
            super.onStop()
            mapView?.onStop()
        }

        override fun onLowMemory() {
            super.onLowMemory()
            mapView?.onLowMemory()
        }

        override fun onDestroy() {
            super.onDestroy()
            mapView?.onDestroy()
        }
}

