class User:
    """ User in the database """

    def __init__(self, _name=None, _password=None):
        """ Inits a user """

        if not _name or not _password:
            print('You must input name and password')
            return

        if len(_name) > 20:
            print('Name must be shorter than 20 symbols')
            return
        
        if len(_password) < 4 or len(_password) > 20:
            print('Password must has length from 4 to 20 symbols')
            return

        self.__name = _name
        self.__password = _password

    
    def get_name(self):
        """ Returns username """

        return self.__name

    
    def get_password(self):
        """ Returns password """

        return self.__password
