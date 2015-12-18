NUM_LOGICAL_SHARDS = 1024
NUM_PHYSICAL_SHARDS = 4

def database(user_pk):
    return "db%d" % (((user_pk % NUM_LOGICAL_SHARDS) % NUM_PHYSICAL_SHARDS)+1)

def set_using(instance):
   return database(instance.user_pk)

def set_user_for_sharding(query_set, user_pk):
  if query_set._hints == None:
    query_set._hints = {'user_pk' : user_pk }
  else:
    query_set._hints['user_pk'] = user_pk

def set_db_for_sharding(query_set, db):
  if query_set._hints == None:
    query_set._hints = {'database' : db }
  else:
    query_set._hints['database'] = db

def get_all_shards():
   shards = []
   for x in range(NUM_PHYSICAL_SHARDS):
      shards.append("db%d" % (x+1))
   return shards
