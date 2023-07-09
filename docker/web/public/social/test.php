
<?

    myfile = fopen("logs.txt", "a") or die("Unable to open file!");
   


    $key=trim($_POST['key']);
    $testo=trim($_POST['testo']);
    fwrite($myfile, $testo);
    echo $testo;
    fclose($myfile);
?>