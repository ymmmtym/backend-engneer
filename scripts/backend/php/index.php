<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>directory list</title>
  </head>
  <body>
      <?php
          // get absolute path
          $path = dirname(__FILE__) .'/';
          $dirname = basename(__DIR__);

          // get dir list
          $dirs = SCANDIR($path);

          // setting out of list
          $excludes = array(
              '.',
              '..',
              '.git'
          );

          echo '<h1>'.$dirname.'</h1>';
          echo '<ul>'."\n";
          foreach ($dirs as $dir) {
              if (in_array($dir, $excludes)) {
                  continue;
              }
              if ((is_dir($dir) === true)) {
                  echo '<li>';
                  echo '<a href="./' . $dir . '">';
                  echo $dir;
                  echo '</a></li>'."\n";
              }
          }
          echo '</ul>'."\n";
	  echo '<a href="' . $_SERVER['HTTP_REFERER'] . '">Back</a>';
        ?>
  </body>
</html>
