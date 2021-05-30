from sqlalchemy import *
from base import Base

# TransferPlots object definition        
class PlotFile(Base):
    __tablename__ = 'plot_file'

    id                       = Column(Integer, primary_key=True)
    from_hostname            = Column(String(12))
    plot_name                = Column(String(255))
    plot_size                = Column(Integer)
    to_path                  = Column(String(255))
    status                   = Column(String(12))
    transfer_start_time      = Column(DateTime)
    transfer_end_time        = Column(DateTime)
    transfer_total_time      = Column(Integer)
    update_datetime          = Column(DateTime)
      
    def __repr__(self):
        return "<PlotFile(plot_name='%s')>" % (self.plot_name)