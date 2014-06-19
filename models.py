'''Models definitions and related utilities'''

from google.appengine.ext import ndb
from google.appengine.api import memcache
import functools

@ndb.transactional
def index_ndb_transactional(doc_id, timeout=1):
  '''
  Decorator for transactionally changing indexed documents
  (google.appengine.api.search) and datastore entities 
  (google.appengine.ext.ndb) together.

  Args:
    doc_id: the document_id (or an iterable of ids) that will be changed by the transaction
    timeout: the maximum number of seconds to wait to acquire a lock on the document(s) (default: 1)

  Only certain types of index operations are supported. Follow these 
  rules to ensure that all changes in the decorated function are transactional:
  - Always make index changes LAST in the decorated function
  - Only make ONE index change per transaction. If you need to put
    multiple documents, provide an iterable of documents to index.put().
    Mixed puts and deletes are not supported.

  If any of these rules is violated, transactionality 
  in the decorated function cannot be guaranteed.
  '''

  #TODO: TEST
  def transactional_wrapper(func):
    @functools.wraps(func)
    def inner_inner(*args, **kwargs):
      #get memcache lock (throw error if wait is too long)
      key = 'trans_lock_' + doc_id
      client = memcache.Client()
      while True:
        lock = client.gets(key)
        if lock:
          continue
        elif client.cas(key, 'arbitrary payload')
          break

      try:
        func(*args, **kwargs)
      except:
        raise ndb.rollback
        # TODO: log error
      finally:
        #release lock
        client.delete(key)

    return inner_inner
  return inner
