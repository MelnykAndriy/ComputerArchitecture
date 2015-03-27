<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>{{title}}</title>
    <style>
        input.bigbutton {
            width:500px;
            background: #3e9cbf; /*the colour of the button*/
            padding: 8px 14px 10px; /*apply some padding inside the button*/
            border:1px solid #3e9cbf; /*required or the default border for the browser will appear*/
            cursor:pointer; /*forces the cursor to change to a hand when the button is hovered*/
            /*style the text*/
            font-size:1.5em;
            font-family:Oswald, sans-serif; /*Oswald is available from http://www.google.com/webfonts/specimen/Oswald*/
            letter-spacing:.1em;
            text-shadow: 0 -1px 0px rgba(0, 0, 0, 0.3); /*give the text a shadow - doesn't appear in Opera 12.02 or earlier*/
            color: #fff;
            /*use box-shadow to give the button some depth - see cssdemos.tupence.co.uk/box-shadow.htm#demo7 for more info on this technique*/
            -webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;
            box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;
            /*give the corners a small curve*/
            -webkit-border-radius: 10px;
            border-radius: 10px;
        }
        /***SET THE BUTTON'S HOVER AND FOCUS STATES***/
        input.bigbutton:hover, input.bigbutton:focus {
            color:#dfe7ea;
            /*reduce the size of the shadow to give a pushed effect*/
            -webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;
            box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;
        }
        #base_container { height:600px; position:relative; }
        #base_content { left:50%; top:50%; transform:translate(-50%,-50%); -webkit-transform:translate(-50%,-50%); position:absolute; }
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
</head>
<body id="body_id">
    <input id='home' class="bigbutton" type="button" onclick="document.location.replace('/')" value="Home." style="text-align:center"/>
    <div id="base_container">
        <div id="base_content">
            {{!base}}
        </div>
    </div>
</body>
</html>