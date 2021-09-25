from itertools import chain
import sys
from uuid import uuid4
from dwca.read import DwCAReader
from dwca.darwincore.utils import qualname as qn
import dwca.exceptions
from functools import reduce

def mintId():
	return str(uuid4())

HAD_UNIQUE_KEY_VALUE_SET = "https://github.com/bio-linker/us-dataset-finder/terms#hadUniqueKeyValueSet"
HAD_KEY_VALUE_PAIR = "https://github.com/bio-linker/us-dataset-finder/terms#hadKeyValuePair"
HAD_KEY = "https://github.com/bio-linker/us-dataset-finder/terms#hadKey"
HAD_VALUE = "https://github.com/bio-linker/us-dataset-finder/terms#hadValue"

setOfElements=set()
keyFieldNames = {
	'http://rs.tdwg.org/dwc/terms/country',
	'http://rs.tdwg.org/dwc/terms/stateProvince',
	'http://rs.tdwg.org/dwc/terms/institutionId',
	'http://rs.tdwg.org/dwc/terms/institutionCode',
	'http://rs.tdwg.org/dwc/terms/locationId',
	'http://rs.tdwg.org/dwc/terms/continent',
	'http://rs.tdwg.org/dwc/terms/countryCode',
	'http://rs.tdwg.org/dwc/terms/county',
	'http://rs.tdwg.org/dwc/terms/municipality',
	'http://rs.tdwg.org/dwc/terms/locality',
	'http://rs.tdwg.org/dwc/terms/verbatimLocality'
}

try:
	# fileName="dwca.zip"
	fileName=sys.argv[1]
	datasetHash=sys.argv[2]

	# Do not uncomment me ## listOfUSATerms = ['USA', 'usa', 'united states of america', 'United States of America', 'UNITED STATES OF AMERICA', 'UNITED STATES', 'united states', 'United States', 'US', 'us']
	with DwCAReader(fileName) as dwca:
		for core_row in dwca:
			for row in chain([core_row], core_row.extensions):
				if row.rowtype == 'http://rs.tdwg.org/dwc/terms/Occurrence':
					rowKeyFieldNames = [fieldName for fieldName in keyFieldNames if fieldName in row.data]
					keyFieldValues=[row.data[fieldName] for fieldName in rowKeyFieldNames]
					if len(keyFieldValues)>0:
						stringToHash = reduce(lambda a, b: a + b, keyFieldValues)
						if stringToHash not in setOfElements and stringToHash!="":
							setOfElements.add(stringToHash)
							uniqueKeyValuePairsId=mintId()
							print('<{}> <{}> <{}> .'.format(datasetHash, HAD_UNIQUE_KEY_VALUE_SET, uniqueKeyValuePairsId))
							for fieldName in rowKeyFieldNames:
								newId=mintId()
								print('<{}> <{}> <{}> .'.format(uniqueKeyValuePairsId, HAD_KEY_VALUE_PAIR, newId))
								print('<{}> <{}> "{}" .'.format(newId, HAD_KEY, fieldName))
								print('<{}> <{}> "{}" .'.format(newId, HAD_VALUE, row.data[fieldName]))

except dwca.exceptions.InvalidArchive:
 	pass
except AttributeError:
	pass
except Exception as e:
	raise e