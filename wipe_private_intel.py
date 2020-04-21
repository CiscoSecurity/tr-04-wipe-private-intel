import sys
from threatresponse import ThreatResponse

def build_object(obj, entity, command):
    '''Recursively build the object needed to query Private Intel
    '''
    entity = entity.replace('-', '_')
    attributes = f'private_intel.{entity}.{command}'.split(".")
    for i in attributes:
        obj = getattr(obj, i)
    return obj

def extract_ids(response):
    '''Parse the Private Intel response and extract the Entity IDs
    '''
    return [entity['id'] for entity in response]

def search(obj, query='*'):
    '''Search Private Intel using a default wildcard query if no query is specified
    '''
    parameters = {'query':query}
    response = obj(params=parameters)
    return response

def delete(obj, ids):
    '''Delete Entities from Private Intel
    '''
    for entity_id in ids:
        print(f'  Deleting {entity_id}', end=' ')
        response = obj(entity_id)
        if response.status_code == 204:
            print('- DONE!')
        else:
            print('- Failed!') # An issue with the Python module causes this to never working

def confirm_continue():
    '''Ask the user if they want to continue
       Keep asking until the input starts with  'y', 'Y', 'n', or 'N'
    '''
    while True:
        reply = str(input('Are you sure you want to continue? (y/n): ')).lower().strip()
        if reply[:1] == 'y': # using [:1] instead of [0] prevents IndexError if the reply is empty
            print()
            return True
        if reply[:1] == 'n':
            return False

def main():
    '''The main script logic
    '''

    # Warn user and verify that you want to continue
    print('-=== WARNING THIS SCRIPT WILL DELETE THINGS ===-')
    if not confirm_continue():
        sys.exit("Bye!")

    # Threat Response Credentials
    tr_client_id = 'client-asdf12-34as-df12-34as-df1234asdf12'
    tr_client_password = 'asdf1234asdf1234asdf1234asdf1234asdf1234asdf1234asdf12'

    # Instantiate Threat Response client
    client = ThreatResponse(
        client_id=tr_client_id,
        client_password=tr_client_password
    )

    # Define CTIM entities to delete
    entities = [
        'actor',
        'attack-pattern',
        'campaign',
        'casebook',
        'coa',
        'incident',
        'indicator',
        'judgement',
        'malware',
        'relationship',
        'sighting',
        'tool',
        'weakness'
    ]

    # Store response from second confirmation to continue
    delete_objects = False

    for entity in entities:
        print(entity)

        # Build Private Intel search objects
        obj = build_object(client, entity, 'search')

        # Search Private Intel for entity
        # A time range can be submitted as the query to delete entities within that range
        # response = search(obj, 'timestamp:["2020-01-01T01:00:00.000Z" TO "2020-03-31T00:00:00.000Z"]')
        response = search(obj)

        # Extract IDs from response
        ids = extract_ids(response)

        # Print number of IDs found
        print('  Found:', len(ids))

        # Build Private Intel delete objects
        obj = build_object(client, entity, 'delete')

        # Warn user and verify that you want to continue
        if not delete_objects and len(ids) > 0:
            print('\n-=== FINAL WARNING CONTINUING WILL DELETE EVERYTHING FOUND ===-')
            print('-===         WILL NOT ASK AGAIN FOR OTHER ENTITIES         ===-')
            if not confirm_continue():
                sys.exit("Bye!")
            else:
                delete_objects = True

        # Delete the entities
        delete(obj, ids) # UNCOMMENT TO DELETE STUFF

if __name__ == '__main__':
    main()
