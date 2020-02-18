<?php
  function replace($str) {
    $subject = array(",","、", "・");
    $replace = "\n";
    return (str_replace($subject, $replace, $str));
  }

  echo (replace("会社名・会社名・会社名・会社名・"));
?>
