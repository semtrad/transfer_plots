from sqlalchemy import *
from base import Base

# TransferPlots object definition        
class TransferPlots(Base):
    __tablename__ = 'transfer_plots'

    id                       = Column(Integer, primary_key=True)
    from_hostname            = Column(String(12))
    from_path                = Column(String(255))
    plot_name                = Column(String(255))
    plot_size                = Column(Integer)
    to_path                  = Column(String(255))
    status                   = Column(String(12))
    trasferred               = Column(Boolean)
    update_datetime          = Column(DateTime)
      
    def __repr__(self):
        return "<TransferPlots(plot_name='%s')>" % (self.plot_name)