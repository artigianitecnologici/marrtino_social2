<?php

include("system_header.php");

	
$_SESSION['session_admin'] = '';
$_SESSION['session_return_url'] = '';
$_SESSION['session_secret'] = '';

// if $gallery_url is site root, then this is empty '', so redirect to '/'
if($gallery_url==''){
	header("Location: ".$gallery_url."/?message=you are logged out&message_type=success");
	exit;
}

header("Location: ".$gallery_url."?message=you are logged out&message_type=success");
exit;

?>