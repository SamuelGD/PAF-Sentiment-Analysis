

function triggerFromSend( user )
{

   var message = document.getElementById("monInput").value;

   document.getElementById("monInput").value = "";

   if( message == "" )
   {

    alert( "Veuillez entrer du texte avant d'appuyer sur le bouton Send.....");

   }
   else
   {

   request( getScore , message );

    }

}


function bottom() 
{

    document.getElementById( 'bottom' ).scrollIntoView();
    window.setTimeout( function () { top(); }, 2000 );


};


      function getXMLHttpRequest() {
  var xhr = null;
  
  if (window.XMLHttpRequest || window.ActiveXObject) {
    if (window.ActiveXObject) {
      try {
        xhr = new ActiveXObject("Msxml2.XMLHTTP");
      } catch(e) {
        xhr = new ActiveXObject("Microsoft.XMLHTTP");
      }
    } else {
      xhr = new XMLHttpRequest(); 
    }
  } else {
    alert("Votre navigateur ne supporte pas l'objet XMLHTTPRequest...");
    return null;
  }
  
  return xhr;
}

function request(callback , chain) {

  var xhr = getXMLHttpRequest();
  
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && (xhr.status == 200 || xhr.status == 0)) {
      callback(xhr.responseText);
    }
  };

  var classPython = "class";

  classPython = getParameterByName(classPython);

  
  xhr.open("GET", "handle_opinion.php?text=" + chain + "&class=" + classPython, true);
  xhr.send(null);


}
  
  


function requestAdd(message , user , score ) {

  var xhr = getXMLHttpRequest();

  xhr.open("GET", "add_message.php?message=" + message + "&user=" + user + "&score=" + score , true);
  xhr.send(null);
  
  
}

function readData(sData)
{

  var tableau = sData.split(";");

  var monScore = parseInt(tableau[0]);

  var old = document.getElementById("container").innerHTML;

  if( monScore == 0 )
  {

    

   document.getElementById("container").innerHTML = old.replace( "<div id=\"bottom\"></div>" , "") + "<li class=\"left clearfix\"><span class=\"chat-img pull-left\"><img style=\" width: 50px; height: 50px; \" src=\"emoticone/neutre\" alt=\"User Avatar\" class=\"img-circle\" /></span><div class=\"chat-body clearfix\"><div class=\"header\"><strong class=\"primary-font\">Him</strong> <small class=\"pull-right text-muted\"><span class=\"glyphicon glyphicon-time\" style=\"visibility: hidden;\"></span></small></div><p>" + sData +  "</p></div></li>" + "<div id=\"bottom\"></div>";

         

  }
  else if( monScore > 0 )
  {

    document.getElementById("container").innerHTML = old.replace( "<div id=\"bottom\"></div>" , "") + "<li class=\"left clearfix\"><span class=\"chat-img pull-left\"><img style=\" width: 50px; height: 50px; \" src=\"emoticone/content\" alt=\"User Avatar\" class=\"img-circle\" /></span><div class=\"chat-body clearfix\"><div class=\"header\"><strong class=\"primary-font\">Him</strong> <small class=\"pull-right text-muted\"><span class=\"glyphicon glyphicon-time\" style=\"visibility: hidden;\"></span></small></div><p>" + sData +  "</p></div></li>" + "<div id=\"bottom\"></div>";

  }
  else if( monScore < 0)
  {

    document.getElementById("container").innerHTML = old.replace( "<div id=\"bottom\"></div>" , "") + "<li class=\"left clearfix\"><span class=\"chat-img pull-left\"><img style=\" width: 50px; height: 50px; \" src=\"emoticone/enerve\" alt=\"User Avatar\" class=\"img-circle\" /></span><div class=\"chat-body clearfix\"><div class=\"header\"><strong class=\"primary-font\">Him</strong> <small class=\"pull-right text-muted\"><span class=\"glyphicon glyphicon-time\" style=\"visibility: hidden;\"></span></small></div><p>" + sData +  "</p></div></li>" + "<div id=\"bottom\"></div>";


  }

  bottom();


}


function requestMessage( callback , user )
{

    var xhr = getXMLHttpRequest();
  
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4 && (xhr.status == 200 || xhr.status == 0)) {
        callback(xhr.responseText);
      }
    };

    
    xhr.open("GET", "getMessage.php?user=" + user , true);
    xhr.send(null);

}


function readMessage(sData)
{

  var monTableau = sData.split(";");

  if( (monTableau[0] != "nothing") )  
  {

     if( monTableau[2].search( "undefined" ) != 0 )
     {

     read( monTableau[1] , monTableau[2] );

     }

  }

}


function read( score , message )
{

  var monScore = parseInt(score);

  var old = document.getElementById("container").innerHTML;

  if( monScore == 0 )
  {

    

   document.getElementById("container").innerHTML = old.replace( "<div id=\"bottom\"></div>" , "") + "<li class=\"left clearfix\"><span class=\"chat-img pull-left\"><img style=\" width: 50px; height: 50px; \" src=\"emoticone/neutre\" alt=\"User Avatar\" class=\"img-circle\" /></span><div class=\"chat-body clearfix\"><div class=\"header\"><strong class=\"primary-font\">Him</strong> <small class=\"pull-right text-muted\"><span class=\"glyphicon glyphicon-time\" style=\"visibility: hidden;\"></span></small></div><p>" + message +  "</p></div></li>" + "<div id=\"bottom\"></div>";

         

  }
  else if( monScore > 0 )
  {

    document.getElementById("container").innerHTML = old.replace( "<div id=\"bottom\"></div>" , "") + "<li class=\"left clearfix\"><span class=\"chat-img pull-left\"><img style=\" width: 50px; height: 50px; \" src=\"emoticone/content\" alt=\"User Avatar\" class=\"img-circle\" /></span><div class=\"chat-body clearfix\"><div class=\"header\"><strong class=\"primary-font\">Him</strong> <small class=\"pull-right text-muted\"><span class=\"glyphicon glyphicon-time\" style=\"visibility: hidden;\"></span></small></div><p>" + message +  "</p></div></li>" + "<div id=\"bottom\"></div>";

  }
  else if( monScore < 0)
  {

    document.getElementById("container").innerHTML = old.replace( "<div id=\"bottom\"></div>" , "") + "<li class=\"left clearfix\"><span class=\"chat-img pull-left\"><img style=\" width: 50px; height: 50px; \" src=\"emoticone/enerve\" alt=\"User Avatar\" class=\"img-circle\" /></span><div class=\"chat-body clearfix\"><div class=\"header\"><strong class=\"primary-font\">Him</strong> <small class=\"pull-right text-muted\"><span class=\"glyphicon glyphicon-time\" style=\"visibility: hidden;\"></span></small></div><p>" + message +  "</p></div></li>" + "<div id=\"bottom\"></div>";


  }

  bottom();


}


function getScore ( opinion )
{

  var tableau = opinion.split(";");

  var score = 0;

  if( tableau[0].search("positive") >= 0 )
  {
    score = 1;
  }
  else if( tableau[0].search("negative") >= 0 )
  {
    score = -1;
  }
  else if( tableau[0].search("neutral") >= 0 )
  {
    score = 0;
  }

  var trend = "trend";

  trend = getParameterByName(trend);

  trend = String( trend );

  if( trend.search("false") == 0 || trend.search("null") == 0 )
  {

  var oldScore = parseInt( document.getElementById('stockage').getAttribute("name") );

  score = score + oldScore;

  score = parseInt( score );

  document.getElementById('stockage').setAttribute("name" , score );

  }


  var old = document.getElementById("container").innerHTML;

  if( score >= 1 )
  {


   document.getElementById("container").innerHTML = old.replace( "<div id=\"bottom\"></div>" , "") + 

         "<li class="+"\""+"right clearfix"+"\""+"><span class="+"\""+"chat-img pull-right"+"\""+"><img style=\" width: 50px; height: 50px; \" src="+"\""+"emoticone/content.png"+"\""+" alt="+"\""+"User Avatar"+"\""+" class="+"\""+"img-circle"+"\""+" /></span><div class="+"\""+"chat-body clearfix"+"\""+"><div class="+"\""+"header"+"\""+"><small class=\"text-muted"+"\""+"><span style=\"visibility: hidden;\" class="+"\""+"glyphicon glyphicon-time"+"\""+"></span></small><strong class="+"\""+"pull-right primary-font"+"\""+">Me</strong></div><p>" + tableau[1] +  "</p></div></li>" + "<div id=\"bottom\"></div>";

    document.getElementById('monInput').value = "";

  }
  else if( score == 0)
  {

    document.getElementById("container").innerHTML = old.replace( "<div id=\"bottom\"></div>" , "") + 

         "<li class="+"\""+"right clearfix"+"\""+"><span class="+"\""+"chat-img pull-right"+"\""+"><img  style=\" width: 50px; height: 50px; \" src="+"\""+"emoticone/neutre.png"+"\""+" alt="+"\""+"User Avatar"+"\""+" class="+"\""+"img-circle"+"\""+" /></span><div class="+"\""+"chat-body clearfix"+"\""+"><div class="+"\""+"header"+"\""+"><small class=\"text-muted"+"\""+"><span style=\"visibility: hidden;\" class="+"\""+"glyphicon glyphicon-time"+"\""+"></span></small><strong class="+"\""+"pull-right primary-font"+"\""+">Me</strong></div><p>" + tableau[1] +  "</p></div></li>" + "<div id=\"bottom\"></div>";

    document.getElementById('monInput').value = "";


  }
  else
  {

    document.getElementById("container").innerHTML = old.replace( "<div id=\"bottom\"></div>" , "") + 

         "<li class="+"\""+"right clearfix"+"\""+"><span class="+"\""+"chat-img pull-right"+"\""+"><img  style=\" width: 50px; height: 50px; \" src="+"\""+"emoticone/enerve.png"+"\""+" alt="+"\""+"User Avatar"+"\""+" class="+"\""+"img-circle"+"\""+" /></span><div class="+"\""+"chat-body clearfix"+"\""+"><div class="+"\""+"header"+"\""+"><small class=\"text-muted"+"\""+"><span style=\"visibility: hidden;\" class="+"\""+"glyphicon glyphicon-time"+"\""+"></span></small><strong class="+"\""+"pull-right primary-font"+"\""+">Me</strong></div><p>" + tableau[1] +  "</p></div></li>" + "<div id=\"bottom\"></div>";

    document.getElementById('monInput').value = "";


  }

  var user = "user";

  var myUser = getParameterByName(user);

  requestAdd( tableau[1] , myUser , score );

  bottom();



}

function getParameterByName(name) {

    var match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search);
    return match && decodeURIComponent(match[1].replace(/\+/g, ' '));

}




