NUM_LOGICAL_SHARDS = 1024
NUM_PHYSICAL_SHARDS = 4

class AuthSessRouter(object):
  def r_w_database(self, model):
    if model._meta.app_label in ('auth', 'sessions'):
      return 'authsess_db'
    return None
  def db_for_read(self, model, **hints):
    return self.r_w_database(model)
  def db_for_write(self, model, **hints):
    return self.r_w_database(model)

class ShardRouter(object):
  def database(self, user_pk):
    return "db%d" % (((user_pk % NUM_LOGICAL_SHARDS) % NUM_PHYSICAL_SHARDS)+1)

  def r_w_database(self, model, **hints):
    db = None    
    try:
      instance = hints['instance']
      db = self.database(instance.user_pk)
    except AttributeError:
      db = self.database(instance.id)
    except KeyError:
      print ("No instance found")
    return db

  def db_for_read(self, model, **hints):
    return self.r_w_database(model)
  def db_for_write(self, model, **hints):
    return self.r_w_database(model)

