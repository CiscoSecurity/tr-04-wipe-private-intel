[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Threat-Response "Gitter chat")

### Threat Response Wipe Private Intel:

This script queries the Threat Response [Private Intel API](https://private.intel.amp.cisco.com/index.html) for a defined list of CTIM entities, collects the IDs, and deletes everything. This script is indented for use in development or test environments only. Great care should be taken if using this in a productoin environment as it can delete everything including `casebooks` and `incidents`.

### Before using you must update the following:
- tr_client_id
- tr_client_password

### Usage:
```
python wipe_private_intel.py
```

### Example script output:  
```
-=== WARNING THIS SCRIPT WILL DELETE THINGS ===-
Are you sure you want to continue? (y/n): y

actor
  Found: 0
attack-pattern
  Found: 0
campaign
  Found: 0
casebook
  Found: 0
coa
  Found: 0
incident
  Found: 1

-=== FINAL WARNING CONTINUING WILL DELETE EVERYTHING FOUND ===-
-===         WILL NOT ASK AGAIN FOR OTHER ENTITIES         ===-
Are you sure you want to continue? (y/n): y

  Deleting https://private.intel.amp.cisco.com:443/ctia/incident/incident-bf0135a8-bfc9-4a3d-aa5c-f9c11eafc59d - DONE!
indicator
  Found: 1
  Deleting https://private.intel.amp.cisco.com:443/ctia/indicator/indicator-9dc97c2d-5839-4e32-bc17-f92988b3b5ca - DONE!
judgement
  Found: 1
  Deleting https://private.intel.amp.cisco.com:443/ctia/judgement/judgement-a15eb374-4212-42d2-98f6-307ac3d8b0fc - DONE!
malware
  Found: 1
  Deleting https://private.intel.amp.cisco.com:443/ctia/malware/malware-f1c79d34-0ef7-4857-9aea-35284f81cdcf - DONE!
relationship
  Found: 0
sighting
  Found: 1
  Deleting https://private.intel.amp.cisco.com:443/ctia/sighting/sighting-e4e8fdb7-371f-4dc4-a401-bd662828c24d - DONE!
tool
  Found: 1
  Deleting https://private.intel.amp.cisco.com:443/ctia/tool/tool-4c97f038-32cd-4def-9cfb-3891865f0263 - DONE!
weakness
  Found: 1
  Deleting https://private.intel.amp.cisco.com:443/ctia/weakness/weakness-d1bc5bc4-77fc-4cb7-8cad-62eba8afb8a5 - DONE!
```
