<?php

// configuration
 
$file = 'barzellette.txt';

// check if form has been submitted
if (isset($_POST['text']))
{
    // save the text contents
    file_put_contents($file, $_POST['text']);

    // redirect to form again
    //header(sprintf('Location: %s', $url));
    //printf('<a href="%s">Moved</a>.', htmlspecialchars($url));
    //exit();
}

// read the textfile
$text = file_get_contents($file);

?>
<!-- HTML form -->
<form action="editorbarzellette.php" method="post">
<textarea rows="40" cols="100" name="text"><?php echo $text; ?></textarea>
<br>
<input type="submit" />
<!--<input type="reset default" />-->
</form>
