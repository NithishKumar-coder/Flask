import json

def Get_Entity(entity,fname,folder_name):
        name=get(entity,folder_name)

        if len(name)!=0:
            data_dict={"Entity":entity,"Name_list":name}
            return data_dict
        else:
            return False

 
def get(entity,folder_name):
    name_list=[]
    with open("./"+folder_name+"/all_entities.json") as f:
        data=json.load(f)
        for items in data:
            if entity==items['Entity']:
                if items['Name'] not in name_list:
                    name_list.append(items['Name'])

    return name_list
