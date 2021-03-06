def create_json_base():
    import os
    import json

    workdir = os.getcwd() + '/champion/'    
    champion_objects = {}
    
    for filename in os.listdir(workdir):
        with open(workdir + filename) as json_file:
            champion_objects[ filename.replace(".json", "")] = json.load(json_file)
            
    for key, data in champion_objects.items():
        p = data['data'][key]
        roles = p['tags']
        skins = [skin['name'] for skin in p['skins'] if skin['name'] != 'default']
        champion_objects[key] = {'roles': roles, 'skins': skins}

    #to change into a document db like mongo or cosmos
    with open('db.json', 'w') as file_to_read:
        file_to_read.write(json.dumps(champion_objects, ensure_ascii=False))
                    

def main():
    create_json_base()

    
main()
