from dal.user_dal import UserDal


class UserBll:
    @staticmethod
    def __users_to_dict(users):
        _users = []
        for item in users:
            obj = {
                'id': item.id,
                'email': item.email,
                'created_at': str(item.created_at)
            }
            _users.append(obj)

        return _users

    def get_users(self):
        users = UserDal.get_select()
        if users is None:
            return users
        else:
            return UserBll.__users_to_dict(users)
