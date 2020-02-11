<?php

// 連想配列($array)
$array = array(
  "name" => "yumemo" ,
  "gender" => "unknown" ,
  "favorite" => array(
    "music" => "音楽" ,
    "published" => "2014-06-10" ,
    "url" => "https://hogehoge.jp/" ,
  ),
);

$json1 = json_encode( $array ) ;
echo "連想配列をJSONに変換(エンコード)する\n$json1\n\n";

$json2 = json_encode( $array , JSON_UNESCAPED_UNICODE ) ;
echo "unicodeをescapeしない\n$json2\n\n";

$json3 = json_encode( $array , JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES ) ;
echo "\\をescapeしない\n$json3\n\n";

$json4 = json_encode( $array , JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES ) ;
echo "改行とインデントをつける\n$json4\n\n";

?>
