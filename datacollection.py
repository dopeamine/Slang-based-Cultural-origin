import pandas as pd

test_frame = pd.DataFrame({'id': user.id,
                           'tweets': [s.text for s in statuses],
                           'location':'NC'})