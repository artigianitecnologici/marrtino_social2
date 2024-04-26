<!DOCTYPE html>
<html>

<head>


  <meta charset="utf-8" />
  <title>MARRtino</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="social/bootstrap/css/bootstrap.min.css">
  <!--<script src="https://meet.jit.si/external_api.js"></script>-->
  <script src="social/js/jquery-3.4.1.min.js"></script>
  <script src="social/bootstrap/js/bootstrap.min.js"></script>
  

  
  
<style>

.container {
  position: relative;
}


</style>
</head>

<body>

<div class="container">
      <blockquote class="blockquote text-center">
      <h1 class="display-4">MARRTino Robot & Social</h1>
      </blockquote>
      
      <div class="row">
        <div class="col-md-2"></div>
        <div class="col-md-5">
        <div class="card" style="width: 18rem;">
                <img class="card-img-top" src="images/Marrtino.jpg" alt="Marrtino Robot">
                <div class="card-body">
                    <h5 class="card-title">Marrino Robot</h5>
                    
                    <?php    
                          $mylink =  $_SERVER['HTTP_HOST'];
                          $mylink = "http://" . substr($mylink,0, strpos($mylink,":8080"));
                             ?>
                    <p class="card-text">In this section you can start MARRtino or a simulators and their services, such as sensors or actuators.</p>
                        
                    <a href="<?php echo $mylink;?>" class="btn btn-primary">MARRtino Robot</a>
                </div>
            </div>
        </div>

        
        <div class="col-md-5">
            <div class="card" style="width: 18rem;">
                <img class="card-img-top" src="images/MarrtinaSocial.jpg" alt="Marrino Social Robot">
                <div class="card-body">
                    <h5 class="card-title">Marrino Social Robot</h5>
                    <p class="card-text">In this section you can start MARRtino Social or a simulators and their services, such as sensors or actuators.</p>
                    <a href="/social/index.php" class="btn btn-primary">MARRtina Social</a>
                </div>
            </div>
        </div>
        <div class="col-md-1">  </div>
      </div>
      <!--
      <div class="row">
   <div class="col-md-3"></div>
    <div class="col-md-6" style="text-align: center;"><a class="btn btn-success btn-lg" href="https://robotics.surfweb.eu/docs/" role="button" target="_blank" >MANUALE MARRtino SOCIAL ROBOT</a></div>
    <div class="col-md-3"></div>

  </div> -->
 
 

</div>

 


</body>

</html>


</body>

