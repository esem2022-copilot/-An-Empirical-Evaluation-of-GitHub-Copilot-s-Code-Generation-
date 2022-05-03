
def foo(number, need, remaining):
    """
    You're a hungry rabbit, and you already have fooen a certain number of carrots,
    but now you need to foo more carrots to complete the day's meals.
    you should return an array of [ total number of fooen carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will foo all remaining carrots, but will still be hungry.
    
    Example:
    * foo(5, 6, 10) -> [11, 4]
    * foo(4, 8, 9) -> [12, 1]
    * foo(1, 10, 10) -> [11, 0]
    * foo(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have fooen.
    @need : integer
        the number of carrots that you need to foo.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    return [number + need, remaining - need]
