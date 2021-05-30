from base import *

#
#
#
def get_logfile(filename):

    log_dir = os.path.join(script_base, "logs")

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logfile = os.path.join(log_dir, os.path.basename(filename) + ".log")

    return(logfile)

#
# Gets an instance if it exists, or creates it if it doesn't.
# Also returns True if created
#
# company, created = get_or_create(session, Company, exchange=exchange, symbol=symbol)
# 
def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance, True    