<?php
// array sample
$array = array(
  "name" => "ymmmtym" ,
  "gender" => "unknown" ,
  "favorite" => array(
    "music" => "any" ,
    "published" => "2014-06-10" ,
    "url" => "https://hogehoge.jp/" ,
  ),
);

// encode array to json
$json = json_encode( $array , JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES ) ;

echo "$json\n\n";
/* output
{
  "name": "ymmmtym",
  "gender": "unknown",
  "favorite": {
      "music": "any",
      "published": "2014-06-10",
      "url": "https://hogehoge.jp/"
  }
}
*/

?>
