# First run script
import os
from filelogic import report_reindex_igniter, template_reindex_igniter, parameters_reindex_igniter
from dbconsistency import report_naming, parameters_lang_naming, templates_lang_naming


# Create DB
os.system('python db.py')

# Report base information collector
report_reindex_igniter()
template_reindex_igniter()
parameters_reindex_igniter()

# Generate data for translation data
report_naming()
parameters_lang_naming()
templates_lang_naming()