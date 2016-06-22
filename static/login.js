
var mainUrl = "http://http://192.241.188.10:5000/"
//var mainUrl = "http://localhost:5000/"

var errorMessage = document.getElementById("error");
var login = function() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    result = getHTTPPOST(
            mainUrl + "loginCheck",
            "username=" + username + 
            "&password=" + password
    );
    console.log(result);
    if (result == "1") {
        window.location = "/";
    } else if (result == "0") {
        error.innerHTML = "Invalid credentials";
    }
}


var getHTTPPOST = function(url,request) {
    console.log(url + "?" + request);
    var xHttp = new XMLHttpRequest();
    xHttp.open("POST", url + "?" + request, false);
    xHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xHttp.send(url + "?" + request);
    return xHttp.responseText;
}

/*var getHTTPPOST = function(url,request) {
    console.log(request);
    var xmlHttp = new XMLHttpRequest();
    if ("withCredentials" in xmlHttp) {
        xmlHttp.open( "POST", url, false ); // false for synchronous request
    } else if (typeof XDomainRequest != "undefined") {
        xmlHttp = new XDomainRequest();
        xmlHttp.open("POST",url);
    } else {
        xmlHttp = null;
        console.log("OH DAMMIT");
    }
    xmlHttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlHttp.send(request);
    return xmlHttp.responseText;
}*/

