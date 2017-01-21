#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import serial
import sys, traceback

def create_page( curlatdecimal, curlondecimal, saat ):
	print '''<html>
					  <head>
						<meta name="viewport" content="initial-scale=1.0, user-scalable=no">
						<meta charset="utf-8">
						<title>Drone GPS!</title>
						<style>
						  /* Always set the map height explicitly to define the size of the div
						   * element that contains the map. */
						  #map {
							height: 100%;
						  }
						  /* Optional: Makes the sample page fill the window. */
						  html, body {
							height: 100%;
							margin: 0;
							padding: 0;
						  }
						</style>
					  </head>
					  <body>
						<div id="map"></div>
						<script>

						  function initMap() {
							var myLatLng = {lat:'''
	print str(curlatdecimal)+", lng: " + str(curlondecimal)
	print """};

							var map = new google.maps.Map(document.getElementById('map'), {
							  zoom: 20,
							  center: myLatLng
							});

							var marker = new google.maps.Marker({
							  position: myLatLng,
							  map: map,
							  title: '"""+saat+"""'
							});
						  }
						</script>
						<script async defer
						src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC-n3xxPA6dpDUGKfGTUfh3C8nSpyFoNng&callback=initMap">
						</script>
					  </body>
					</html>
					"""
	return

f = open('gps.txt', 'r')
data=f.read().split(",")
create_page(data[0],data[1],data[2])

