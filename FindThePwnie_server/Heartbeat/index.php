<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$data =  htmlspecialchars($_POST['content'], ENT_QUOTES, 'UTF-8');
$error = "";
$results = print_r($data, true) . "\n";

if (!isset($data)) { $error = ''; }
elseif (empty($data)) { $error = '<font color="red"> Content not accepted.</font>'; }
else {
    $error = '<font color="red">Something went wrong. Are you sure you\'re supposed to be here</font>';

    file_put_contents('heartbeats.txt', $results, FILE_APPEND | LOCK_EX);
}



$html = <<<EOF

<html>
<head>
<body>
<h1>the Security Factory - Send info Tool</h1>
<br><p>
<form method="post">
Content:<br>
<textarea id="content" name="content" rows="2" cols="80"></textarea><br><p>
<input id="submit" type="submit" value="Send">
</form>
$error
</body>
</head>
</html>

EOF;

echo $html;
