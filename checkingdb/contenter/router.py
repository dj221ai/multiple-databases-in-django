class CheckerRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'customers':
            return 'customerdb'
        elif model._meta.app_label == 'userchecking':
            return 'usersdb'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'customers':
            return 'customerdb'
        elif model._meta.app_label == 'userchecking':
            return 'usersdb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'customers' or obj2._meta.app_label == 'customers':
            return True
        elif 'customers' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif obj1._meta.app_label == 'userchecking' or obj2._meta.app_label == 'userchecking':
            return True
        elif 'userchecking' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'customers':
            return db == 'customerdb'
        elif app_label == 'userchecking':
            return db == 'usersdb'
        return None


