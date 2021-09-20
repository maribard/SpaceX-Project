import requests
import json


def add_values_in_dict(sample_dict, key, list_of_values):
    if list_of_values[0] == None:
        list_of_values[0] = 0
    if list_of_values[1] == None:
        list_of_values[1] = 0


    if key not in sample_dict:
        sample_dict[key] = []
        sample_dict[key].extend(list_of_values)
    elif sample_dict[key][1] != None and list_of_values[1] != None:
        sample_dict[key][1] = int(sample_dict[key][1]) + int(list_of_values[1])


    return sample_dict





def most_used_first_stages(number_of_cores, unsuccessful_flights, future_missions):
    query = """query {
        launchesPast {
        mission_name
        rocket {
        rocket_name
        first_stage {
            cores {
            flight
            land_success
            core {
                reuse_count
                status
                id
            }
            }
        }
        second_stage {
            payloads {
            payload_mass_kg
            }
        }
        }
    }
    }"""


    url = 'https://api.spacex.land/graphql/'
    r = requests.post(url, json={'query': query})
    json_data = json.loads(r.text)


    my_dict = dict()


    # this loop fetch a cores
    for n in range(len(json_data['data']['launchesPast'])):
        core_id= json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores'][0]['core']['id']
        reuse_count = json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores'][0]['core']['reuse_count']
        payload_mass_kg = json_data['data']['launchesPast'][n]['rocket']['second_stage']['payloads'][0]['payload_mass_kg']

        #condition if number of payload > 1
        if len(json_data['data']['launchesPast'][n]['rocket']['second_stage']['payloads']) > 1:
            for m in range(1, len(json_data['data']['launchesPast'][n]['rocket']['second_stage']['payloads'])):
                if json_data['data']['launchesPast'][n]['rocket']['second_stage']['payloads'][m]['payload_mass_kg'] != None:
                    payload_mass_kg += json_data['data']['launchesPast'][n]['rocket']['second_stage']['payloads'][m]['payload_mass_kg']



        #condition if we have to exclude unsuccessful flights
        if unsuccessful_flights == 'N':
            if  json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores'][0]['land_success'] == True:
                my_dict = add_values_in_dict(my_dict, core_id, [reuse_count, payload_mass_kg])
        else: 
            my_dict = add_values_in_dict(my_dict, core_id, [reuse_count, payload_mass_kg])





        #condition if number of cores > 1
        if len(json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores']) > 1:
            for o in range(1, len(json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores'])):
                core_id = json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores'][o]['core']['id']
                reuse_count = json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores'][o]['core']['reuse_count']



                #condition if we have to exclude unsuccessful flights
                if unsuccessful_flights == 'N':
                    if  json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores'][0]['land_success'] == 'true':
                        my_dict = add_values_in_dict(my_dict, core_id, [reuse_count, payload_mass_kg])
                else: 
                    my_dict = add_values_in_dict(my_dict, core_id, [reuse_count, payload_mass_kg])




    #sort dict by parameter "reused"
    sorted_dict = sorted(my_dict.items(), key=lambda e: e[1][0], reverse=True)

    #create a OUTPUT like list [tuple[str, int, int]]
    moja_lista = []
    for element in range(len(sorted_dict)):
        tup = sorted_dict[element][0], sorted_dict[element][1][0], sorted_dict[element][1][1]
        moja_lista.append(tup)






    # FUTURE MISIONS
    if future_missions == 'Y':
        list_w_active_status = set()
        for n in range(len(json_data['data']['launchesPast'])):
            if json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores'][0]['core']['status'] == "active":
                id = json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores'][0]['core']['id']
                list_w_active_status.add(id)

            if len(json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores']) > 1:
                for p in range(1, len(json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores'])):
                    if json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores'][p]['core']['status'] == "active":
                        id = json_data['data']['launchesPast'][n]['rocket']['first_stage']['cores'][p]['core']['id']
                        list_w_active_status.add(id)
        
        list_w_active_status2 = []
        for elem in moja_lista:
            if elem[0] == list(list_w_active_status)[0]:
                list_w_active_status2.append(elem)
        

        # number of most reused rocket cores to fetch
        if len(list_w_active_status2) > number_of_cores:
            return list_w_active_status2[0:number_of_cores]

        return list_w_active_status2


    
    # number of most reused rocket cores to fetch
    if len(moja_lista) > number_of_cores:
        return moja_lista[0:number_of_cores]
    return moja_lista



