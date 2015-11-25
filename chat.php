
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Chat</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

<link href="style.css" rel="stylesheet">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
 
<script src="jquery-1.11.3.min.js"></script>
    <!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

<script>

    $( document ).ready(function() {
       
      window.setTimeout("timerRun()",10000);

});


    </script>
    
</head>
<body>
    <div class="container" id="stockage" name="0">
    <div class="row">
        <div class="col-md-5">
            <div class="panel panel-primary">
                <div class="panel-heading" id="accordion">
                    <span class="glyphicon glyphicon-comment"></span> Chat
                    <div class="btn-group pull-right">
                            <span class="glyphicon glyphicon-chevron-down"></span>
                        </a>
                    </div>
                </div>
            <div class="panel-collapse collapse in" id="collapseOne">
                <div class="panel-body">
                    <ul class="chat" id="container">
                        <li class="left clearfix"><span class="chat-img pull-left">
                            <img src="http://placehold.it/50/55C1E7/fff&text=U" alt="User Avatar" class="img-circle" />
                        </span>
                            <div class="chat-body clearfix">
                                <div class="header">
                                    <strong class="primary-font">Computer</strong> <small class="pull-right text-muted">
                                        <span class="glyphicon glyphicon-time" style="visibility: hidden;"></span></small>
                                </div>
                                <p>
                                    You can start your conversation ...
                                </p>
                            </div>
                        </li>
                        
                        <div id="bottom"></div>
                    </ul>
                    
                </div>
                <div class="panel-footer">
                    <div class="input-group">
                        <input id="monInput" type="text" class="form-control input-sm" placeholder="Tapez votre message ici....." />
                        <span class="input-group-btn">
                            <button class="btn btn-warning btn-sm" id="btn-chat" onclick="triggerFromButton();">
                             Send</button>
                        </span>
                    </div>
                </div>
            </div>
            </div>
        </div>
    </div>
</div>



    <script src="chat.js"></script>

    <script>



    function triggerFromButton()
    {

     var user = "user";

     var user = getParameterByName(user);

      triggerFromSend( user );

    }
    
    function timerRun()
    {

    var user = "user";

    var user = getParameterByName(user);

    requestMessage( readMessage , user );

    window.setTimeout( "timerRun()",500 );

    }


    </script>

</body>
</html>
