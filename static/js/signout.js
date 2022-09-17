var signout = document.getElementById("signout")


signout.onclick = function(e) {

    var x = confirm("Login to use this app again. Click OK to sign out.");
    
    if (!x)
    {
        e.preventDefault();
    }

}