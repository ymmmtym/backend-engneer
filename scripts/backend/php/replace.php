<?php
  function replace($str) {
    $subject = array(",","、", "・");
    $replace = "\n";
    return (str_replace($subject, $replace, $str));
  }

  echo (replace("company・company・company・company・"));
?>
