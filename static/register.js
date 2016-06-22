var mainUrl = "http://192.241.188.10:5000/"

var errorMessage = document.getElementById("error");
var register = function() {
    var username = document.getElementById("username").value;
    var password1 = document.getElementById("password1").value;
    var password2 = document.getElementById("password2").value;
    if (password1 != password2) {
        error.innerHTML = "Passwords do not match";
    } else {
        result = getHTTPPOST(
                mainUrl + "registerUser",
                "username=" + username + 
                "&password=" + password1
        );
        console.log(result);
        if (result == "1") {
            window.location = "/";
        } else {
            error.innerHTML = result;
        }
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
