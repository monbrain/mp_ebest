## 매매/취소/정정

# def order(ticker, acntNo, price=0, volume=0, side="매수", type="지정가"):
def order(**kwarg):
    """Order by Ebest
    Args:
        kwarg (dict):
            - ticker
            - acntNo
            - price=0
            - volume=0
            - side="매수"
            - type="지정가"

    Returns:
        [type]: [description]
    """
    ticker = kwarg['ticker'] if 'a' in kwarg else None
    acntNo = kwarg['acntNo'] if 'a' in kwarg else None
    return (ticker, acntNo)


def cancel(**kwarg):
    """Order by Ebest
    Args:
        kwarg (dict):
            - ticker
            - acntNo
            - orderNo

    Returns:
        [type]: [description]
    """
    ticker = kwarg['ticker'] if 'a' in kwarg else None
    acntNo = kwarg['acntNo'] if 'a' in kwarg else None
    orderNo = kwarg['acntNo'] if 'a' in kwarg else None
    return (ticker, acntNo, orderNo)


def revise(**kwarg):
    """Order by Ebest
    Args:
        kwarg (dict):
            - ticker
            - acntNo
            - orderNo
            - volume=0
            - side="매수"
            - type="지정가"

    Returns:
        [type]: [description]
    """
    ticker = kwarg['ticker'] if 'a' in kwarg else None
    acntNo = kwarg['acntNo'] if 'a' in kwarg else None
    orderNo = kwarg['acntNo'] if 'a' in kwarg else None
    return (ticker, acntNo, orderNo)