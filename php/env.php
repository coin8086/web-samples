<!DOCTYPE html>
<html>
  <head>
    <title>Hello</title>
  </head>
  <body>
    <?php
      foreach ($_SERVER as $key => $value)
        echo "{$key} => {$value}<br>";
    ?>
  </body>
</html>

