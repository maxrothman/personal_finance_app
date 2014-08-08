'''Models definitions and related utilities'''

from google.appengine.ext import ndb
from google.appengine.api import memcache
from google.appengine.api import search
import functools, time



class Schema(ndb.Model):
  '''A collection of columns.
  Should always have a TransactionGroup as an ancestor.'''
  columns = ndb.StructuredProperty(Column, repeated=True, required=True)


class Column(ndb.Model):
  '''A column of data attached to transactions'''
  name = ndb.StringProperty(required=True)
  kind = ndb.StringProperty(required=True, choices=column_types.keys())
  validator = ndb.ComputedProperty(lambda self: column_types[self.kind])


def date_validator(val):
  pass

def amount_validator(val):
  pass

def category_validator(val):
  pass

def tag_validator(val):
  pass

def text_validator(val):
  pass

column_types = {
  'date': date_validator,
  'amount': amount_validator,
  'category': category_validator,
  'tag': tag_validator,
  'text': text_validator
}


@ndb.transactional
def index_ndb_transactional(doc_id, timeout=1):
  '''
  Decorator for transactionally changing indexed documents
  (google.appengine.api.search) and datastore entities 
  (google.appengine.ext.ndb) together.

  Args:
    doc_id: the document_id (or an iterable of ids) that will be changed by the transaction
    timeout: the maximum number of seconds to wait to acquire a lock on the document(s) (default: 1)

  Exceptions:
    TransactionTimeout if it takes longer than <timeout> to acquire a lock

  Only certain types of index operations are supported. Follow these 
  rules to ensure that all changes in the decorated function are transactional:
  - Always make index changes LAST in the decorated function
  - Only make ONE index change per transaction. If you need to put
    multiple documents, provide an iterable of documents to index.put().
    Mixed puts and deletes are not supported.

  If any of these rules is violated, transactionality 
  in the decorated function cannot be guaranteed.
  '''

  #TODO: TEST, add logging
  def transactional_wrapper(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
      #get memcache lock
      key = 'doc_lock_' + doc_id
      start = time.time()
      
      #This should also work; add() adds the key IFF it doesn't already exist
      while not memcache.add(key, 'arbitrary payload'):
        if time.time() - start > timeout: raise TransactionTimeout()
        #log
        continue
        #TODO: add wait?

      try:
        func(*args, **kwargs)
      except:
        raise ndb.rollback
        # TODO: log error
      finally:
        #release lock
        client.delete(key)

    return inner
  return transactional_wrapper


def memcache_memoize(expiry=None):
  '''Memoizer using memcache. Cache expiration time is in seconds.'''
  def memoizer(func):
    @functools.wraps
    def inner(*args, **kwargs):
      key = 'memoized_' + func.__name__ + ''.join(args) + ''.join(kwargs)
      data = memcache.get(key)
      if data is not None:
        return data
      else:
        data = func(*args, **kwargs)
        memcache.set(key, data, time=expiry)
        return data


class TransactionTimeout(Exception): pass