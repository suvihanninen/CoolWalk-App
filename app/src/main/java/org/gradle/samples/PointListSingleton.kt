package org.gradle.samples

import com.mapbox.geojson.Feature
import com.mapbox.geojson.FeatureCollection
import com.mapbox.geojson.LineString
import com.mapbox.geojson.Point

object PointListSingleton {
    val routeCoordinates=mutableListOf<Point>()

    fun addpoint(coordRow: List<Double>){
        val latCoord = coordRow[0]
        val lonCoord = coordRow[1]
        routeCoordinates.add(Point.fromLngLat(latCoord, lonCoord))
    }

    var featureLineString = Feature.fromGeometry(LineString.fromLngLats(routeCoordinates))
    var featureCollection = FeatureCollection.fromFeature(featureLineString)
}