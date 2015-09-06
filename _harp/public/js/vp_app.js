$(document).ready(function() {
    // volunteer = $.ajax({ //my ajax request
    //     url: "http://127.0.0.1:8000",
    //     type: "GET",
    //     cache: false,
    //     dataType: "jsonp",
    //     crossDomain: true,
    // }).done(function( data ) {
    //     if ( console && console.log ) {
    //       console.log( data );
    //     }
    //   });
    volunteers = $.getJSON('http://127.0.0.1:8000').done(function(data){
        //console.log(data);
        var fullname = data[1].first_name + ' ' + data[1].last_name;
        var username = data[1].username;
        console.log(fullname);
        $('.fullname').text(fullname);
        $('.username').text(username);
    });
});

