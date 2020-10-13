import cv2
import numpy as np
import os


# 日本語ファイル名も読見とれるようにするためにOverride
def image_read(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    """

    Parameters
    ----------
    filename : str
        file名を含めたfileパス
    flags : int, default cv2.IMREAD_COLOR
        1
    dtype : uint8, default np.uint8

    Returns
    -------
    img : buffer
        デコードしたイメージのbufferを返す。

    See Also
    --------
    cv2.imread method
    """
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


# 日本語ファイル名も読見とれるようにするためにOverride
def imwrite(filename, img, params=None):
    """
    Parameters
    ----------
    filename : str
        パスと拡張子を含めたファイル名
    img : buffer
        画像ファイルのパス
    params: None, default None
        フォーマットを指定する。

    Returns
    -------
    bool
        True if successful, False otherwise.

    Notes
    -----
    params Format-specific parameters encoded as pairs (paramId_1, paramValue_1, paramId_2, paramValue_2, ... .)
    see cv::ImwriteFlags
    """

    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
