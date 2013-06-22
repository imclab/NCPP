# Module holding application constants.

APPLICATION_LABEL = 'ncpp'
CONFIG_FILEPATH = '/usr/local/ocgis/ocgis.cfg'

def enum(**enums):
    return type('Enum', (), enums)

    def isComplete(self):
        if (self.status=='ProcessSucceeded' or self.status=='ProcessFailed' or self.status=='Exception'):
            return True
        elif (self.status=='ProcessStarted'):
            return False
        elif (self.status=='ProcessAccepted' or self.status=='ProcessPaused'):
            return False
        else:
            raise Exception('Unknown process execution status: %s' % self.status)


JOB_STATUS = enum(UNKNOWN='Status Unknown', STARTED='Process Started', RUNNING='Process Running', SUCCESS='Process Succeeded', 
                  FAILED='Process Failed', ACCEPTED='Process Accepted', PAUSED='ProcessPaused', ERROR='Error')
