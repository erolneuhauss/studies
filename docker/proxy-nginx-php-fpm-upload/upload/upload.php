<?php  #### upload.php ####

function save_uploaded_file($source, $target, $overwrite=0)
{
    # $overwrite == 0 -> no overwrite, only create if not exists
    # $overwrite == 1 -> open only if exists, overwrite, truncate!
    # $overwrite == 2 -> rewrite existing or create new

    # we believe that php will not produce 'lost handles' if we leave
    # this function without closing them.

    if (!is_int($overwrite)) return 12;

    # open source
    if (!$fs = fopen($source, 'rb')) return 5;
    if (!flock($fs, LOCK_SH)) return 6; ## Source could not be locked;

    # open target

    switch ($overwrite)
    {
        case 0:
            if (!$ft = fopen($target, 'xb'))  return 3;  ## assumed 'already exists'
        break;

        case 1:
            if (!$ft = fopen($target, 'rb+')) return 2;  ## assumed 'not found'
        break;

        case 2:
            if (!$ft = fopen($target, 'wb'))  return 5;  ## assumed 'could not open'
        break;

        default:
            return 12;
    }

    if (!flock($ft, LOCK_EX)) return 6;          ## Target could not be locked;

    $filesize = filesize($source);
    $cont = fread($fs, $filesize);
    if (strlen($cont) != $filesize) return 4;

    fwrite($ft, $cont);

    fclose($fs);

    ## new file perhaps is shorter than old one
    ftruncate($ft, $filesize);
    fclose($ft);

    return 0;
}

if (!empty($_FILES))
{
    echo "<pre>\r\n";
    echo htmlspecialchars(print_r($_FILES,1));
    echo "</pre>\r\n";
}

?>
