
class ZeroNamelengthError(Exception):pass
class SpaceError(Exception):pass
class InvalidError(Exception):pass
class InsufficientFundError(Exception):pass
def validation(name):
    while True:
        if len(name)==0:
            raise ZeroNamelengthError
        else:
            words=name.split()
            if len(words)==0:
                raise SpaceError
            else:
                for word in words:
                    if not word.isalpha():
                        raise InvalidNameError
                    else:
                        return name
                    break



def amount(amou):
    if amou-500>500:
        return amou
    else:
        raise InsufficientFundError