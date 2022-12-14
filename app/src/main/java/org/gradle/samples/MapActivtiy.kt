package org.gradle.samples

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.textfield.TextInputEditText
import com.google.android.material.textfield.TextInputLayout
import com.google.gson.GsonBuilder
import com.mapbox.maps.MapView
import com.mapbox.maps.Style
import okhttp3.Call
import okhttp3.Callback
import okhttp3.OkHttpClient
import okhttp3.Request
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
    }


    fun fetchGeoJson(from: String?, to: String?) {
        val fromNode: Int? = from?.toInt()
        val toNode: Int? = to?.toInt()
        println("Fetching JSON now $from and $to")

        val url = "http://10.0.2.2:5000/coolwalk?fro=${fromNode}&to=${toNode}"

        //Make a okHttp client
        val client = OkHttpClient()

        val request = Request.Builder().url(url).build()

        client.newCall(request).enqueue(object : Callback {

            override fun onFailure(call: Call, e: IOException) {
                println("Request failed ${e.localizedMessage}")
            }

            override fun onResponse(call: Call, response: okhttp3.Response) {

                val gson = GsonBuilder()
                val body = response.body?.string()

                val startTime = System.currentTimeMillis()
                val response = gson.create().fromJson(body, Response::class.java)
                val elapsedTime = System.currentTimeMillis() - startTime
                println("Total elapsed http request/response time in milliseconds: $elapsedTime")

                val coordsList =  response.features[0].geometry.coordinates
                val itr = coordsList.listIterator()
                while (itr.hasNext()) {
                    PointListSingleton.addpoint(itr.next())
                }

                runOnUiThread {}
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

