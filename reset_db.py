import os
import sqlite3


with sqlite3.connect('lms.db') as conn:
    c = conn.cursor()
    c.execute('DELETE FROM raft_logs;')
    c.execute('UPDATE state_info SET term = 0 , idx = 0 , voted_for = null;')
    c.execute('DELETE FROM queries;')
    c.execute('DELETE FROM assignment_submissions;')
    os.rename('Resources','Resources_Old')
    conn.commit()
