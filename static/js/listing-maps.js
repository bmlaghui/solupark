! function(e) {
    "use strict";
    var a = document.getElementById("myMap");
    void 0 !== a && null != a && google.maps.event.addDomListener(window, "load", function (listener) {
        function a(e, t, a, l, s, i, o, n, r) {
            return '<div class="map-info-popup"><div class="item-popup-box"><span class="close-info"><i class="la la-close"></i></span><a href="#" class="map-badge">' + t + '</a><a href="' + e + '" class="map-img-box position-relative d-block"><img src="' + a + '" alt=""></a> <div class="item-list-content position-relative"><h4 class="mb-2"><a href=' + e + ">" + l + '</a></h4><div class="item-ratting mb-3" data-star-rating="' + n + '"><span class="map-review-count">' + r + ' reviews</span></div><span class="location-info d-block mb-2"><i class="la la-map-marker"></i>' + s + '</span><span class="item-call d-block mb-2"><i class="la la-phone"></i><a href="#">' + i + '</a></span><span class="item-call d-block"><i class="la la-clock-o"></i>' + o + "</span></div></div></div>"
        }
        var
            s = new google.maps.Map(document.getElementById("myMap"), {
                zoom: 13,
                scrollwheel: !1,
                mapTypeId: google.maps.MapTypeId.ROADMAP,
                zoomControl: !0,
                mapTypeControl: !1,
                fullscreenControl: !0,
                styles: [{
                    featureType: "water",
                    elementType: "geometry",
                    stylers: [{
                        color: "#e9e9e9"
                    }, {
                        lightness: 17
                    }]
                }, {
                    featureType: "landscape",
                    elementType: "geometry",
                    stylers: [{
                        color: "#f5f5f5"
                    }, {
                        lightness: 20
                    }]
                }, {
                    featureType: "road.highway",
                    elementType: "geometry.fill",
                    stylers: [{
                        color: "#ffffff"
                    }, {
                        lightness: 17
                    }]
                }, {
                    featureType: "road.highway",
                    elementType: "geometry.stroke",
                    stylers: [{
                        color: "#ffffff"
                    }, {
                        lightness: 29
                    }, {
                        weight: .2
                    }]
                }, {
                    featureType: "road.arterial",
                    elementType: "geometry",
                    stylers: [{
                        color: "#ffffff"
                    }, {
                        lightness: 18
                    }]
                }, {
                    featureType: "road.local",
                    elementType: "geometry",
                    stylers: [{
                        color: "#ffffff"
                    }, {
                        lightness: 16
                    }]
                }, {
                    featureType: "poi",
                    elementType: "geometry",
                    stylers: [{
                        color: "#f5f5f5"
                    }, {
                        lightness: 21
                    }]
                }, {
                    featureType: "poi.park",
                    elementType: "geometry",
                    stylers: [{
                        color: "#dedede"
                    }, {
                        lightness: 21
                    }]
                }, {
                    elementType: "labels.text.stroke",
                    stylers: [{
                        visibility: "on"
                    }, {
                        color: "#ffffff"
                    }, {
                        lightness: 16
                    }]
                }, {
                    elementType: "labels.text.fill",
                    stylers: [{
                        saturation: 36
                    }, {
                        color: "#333333"
                    }, {
                        lightness: 40
                    }]
                }, {
                    elementType: "labels.icon",
                    stylers: [{
                        visibility: "off"
                    }]
                }, {
                    featureType: "transit",
                    elementType: "geometry",
                    stylers: [{
                        color: "#f2f2f2"
                    }, {
                        lightness: 19
                    }]
                }, {
                    featureType: "administrative",
                    elementType: "geometry.fill",
                    stylers: [{
                        color: "#fefefe"
                    }, {
                        lightness: 20
                    }]
                }, {
                    featureType: "administrative",
                    elementType: "geometry.stroke",
                    stylers: [{
                        color: "#fefefe"
                    }, {
                        lightness: 17
                    }, {
                        weight: 1.2
                    }]
                }]
            });
        var marker = new google.maps.Marker({
    position: new google.maps.LatLng(48.9149853, 2.349608 ),
    map: s,
    title: "Locronan - Rue du Prieuré"
});
        google.maps.event.addListener(marker, 'click', function () {
            $('#loginModal').modal('show');
        });

        if (navigator.geolocation) {
     navigator.geolocation.getCurrentPosition(function (position) {
         var initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
         console.log(position.coords.latitude)
         console.log(position.coords.longitude)
         s.setCenter(initialLocation);
     });


 }

    })
}(this.jQuery);