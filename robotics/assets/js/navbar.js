var path = window.location.pathname;
$(document).ready(function(){
    if(path == "/index.php"){
        $("#home").addClass("active"); 
    } 
    else if(path == "/about.php"){
        $("#about").addClass("active");
    } 
    else if(path == "/frc.php"){
        $("#frc").addClass("active");
    } 
    else if(path == "/ftc.php"){
        $("#ftc").addClass("active");
    } 
    else if(path == "/outreach.php"){
        $("#outreach").addClass("active");
    }
    else if(path == "/sponsors.php"){
        $("#sponsors").addClass("active");
    }
    else if(path == "/contact.php"){
        $("#contact").addClass("active");
    }

});

