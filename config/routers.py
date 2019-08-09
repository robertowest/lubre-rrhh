class DefaultRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'firebird':
            return 'firebird'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'firebird':
            return 'firebird'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'firebird' or \
            obj2._meta.app_label == 'firebird':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'firebird':
            return db == 'firebird'
        return None

class MySQLRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'rrhh':
            return 'mysql'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'rrhh':
            return 'mysql'
        return None

    def allow_relation(self, elem1, elem2, **hints):
        if elem1._meta.app_label == 'rrhh' or elem2._meta.app_label == 'rrhh':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'rrhh':
            return db == 'mysql'
        return None
