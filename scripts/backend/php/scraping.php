<?php

  $url = $argv[1];
  $src = file($url);
  $implodeSource = implode( "", $src ) ;
  $trimSource = preg_replace( "/(n|r|t)/", "", $implodeSource );
  preg_match_all( "/<h[1-5]>(.*?)<\/h[1-5]>/i", $trimSource, $matches ) ;

  foreach($matches[0] as $match){
      echo $match;
      echo "\n";
  }

  print_r($matches);

?>
