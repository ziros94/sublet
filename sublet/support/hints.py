#tag query_set with user_pk, so routers know where to find it
def set_user_for_sharding(query_set, user_pk):
  if query_set._hints == None:
    query_set._hints = {'user_pk' : user_pk }
  else:
    query_set._hints['user_pk'] = user_pk

