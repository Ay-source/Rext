var signout = document.getElementById("signout")

if (signout) {
    signout.onclick = function(e) {

        var x = confirm("Login to use this app again. Click OK to sign out.");
        
        if (!x)
        {
            e.preventDefault();
        }

    }
}

var form = document.getElementById("form1")

if (form)
{
    form.onsubmit = function(e) {
        var pass = document.getElementsByName("password")[0].value
        var pass_rep = document.getElementsByName("password_repeat")[0].value
        console.log(pass)
        console.log(pass_rep)
        if (pass != pass_rep){
            e.preventDefault()
            console.log("never")
        }
    }
}