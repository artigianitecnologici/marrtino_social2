<?php
    try {
        $dsn = 'mysql:host=mysql;dbname=test;charset=utf8;port=3306';
        $pdo = new PDO($dsn, 'dev', 'dev');
        echo "connesso a db";
    } catch (PDOException $e) {
        echo $e->getMessage();
    }
?>

