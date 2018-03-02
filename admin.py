from user import User
from user import comment

class Admin(User):

    def __init__(self):
        super(Admin, self).__init__(self, id)
        self.id = None
        
    def edit_comment(self, id):
        self.id = id
        edit(comment[id])

 




    

