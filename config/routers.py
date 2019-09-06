MYSQL_APPS = ['auth', 'contenttypes', 'admin', 'sessions', 'rrhh', 'blog']
FIREBIRD_APPS = ['firebird', 'clientes']


class MySQLRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in MYSQL_APPS:
            return 'mysql'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in MYSQL_APPS:
            return 'mysql'
        return None

    def allow_relation(self, elem1, elem2, **hints):
        if elem1._meta.app_label == 'rrhh' or elem2._meta.app_label == 'rrhh':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in MYSQL_APPS:
            return db == 'mysql'
        return None


class FirebirdRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in FIREBIRD_APPS:
            return 'firebird'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in FIREBIRD_APPS:
            return 'firebird'
        return None

    def allow_relation(self, elem1, elem2, **hints):
        if elem1._meta.app_label == 'firebird' or elem2._meta.app_label == 'firebird':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in FIREBIRD_APPS:
            return db == 'firebird'
        return None
