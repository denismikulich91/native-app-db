import sqlite3
import json
import datetime
import math

DB_PATH = 'E:\\MDA\Beta Testing\\Scripting\\native_app_db\\ug_design.db'
# Connect to SQLite database
conn = sqlite3.connect(DB_PATH)

# Create a cursor
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS parameters
             (user_name text, parameters_dict text, mod_date text)''')

def insert_parameters(user_name, parameters_dict, mod_date):
    # Convert the dictionary into a JSON string
    parameters_dict = json.dumps(parameters_dict)

    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)

    # Create a cursor
    c = conn.cursor()

    # Insert a row of data
    c.execute("INSERT INTO parameters VALUES (?, ?, ?)", (user_name, parameters_dict, mod_date))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()
    
def get_parameters(field, parameter_value):
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)

    # Create a cursor
    c = conn.cursor()

    # Get data
    c.execute(f'SELECT * FROM parameters WHERE {field}=?', (parameter_value,))

    # Fetch all rows
    rows = c.fetchall()

    # Close the connection
    conn.close()

    # Convert JSON string back to dictionary
    for row in rows:
        parameters_dict = json.loads(row[1])

    return rows
  
def delete_records(user_name):
    conn = sqlite3.connect(DB_PATH)  # Connect to the database
    cursor = conn.cursor()  # Get a cursor object

    # SQL query string
    sql = '''DELETE FROM parameters WHERE user_name=?'''
    cursor.execute(sql, (user_name,))

    conn.commit()  # Commit the changes
    conn.close()  # Close the connection
    
    
all_attributes = dict()
global_attribute_set = dict()
undercut_attribute_set = dict()
loading_attribute_set = dict()
profile =dict()
totals = dict()

root=ekl.GetEditorRoots("VPMReference").GetItem(1)
all_attributes['site_name'] = str(root.Name)
all_children = root.Children.GetItem(1)
parameters = all_children.Query("AdvisorParameterSet", "x.Name.Search('global')>=0").GetItem(1)
global_attribute_set['tunnel_spacing'] = [float(parameters.GetAttributeReal("tunnel_spacing")), 'm']
global_attribute_set['tunnel_width'] = [float(parameters.GetAttributeReal("tunnel_width")), 'm']
global_attribute_set['number_of_tunnels'] = [float(parameters.GetAttributeReal('number_of_tunnels')), '']

profile['tunnel_width'] = float(parameters.GetAttributeReal('tunnel_width'))
profile['tunnel_height'] = float(parameters.GetAttributeReal('tunnel_height'))
profile['tunnel_r'] = float(parameters.GetAttributeReal('tunnel_r'))

all_attributes['global'] = global_attribute_set
totals['draw_points_number'] = [float(parameters.GetAttributeReal('draw_points_number')), '']
totals['total_dev_length'] = [round(float(parameters.GetAttributeReal('total_dev_length')), 1), 'm']

parameters = all_children.Query("AdvisorParameterSet", "x.Name.Search('undercut')>=0").GetItem(1)
  
undercut_attribute_set['elevation'] = [float(parameters.GetAttributeReal("elevation")), 'm']
undercut_attribute_set['geology_offset'] = [float(parameters.GetAttributeReal("geology_offset")), 'm']
undercut_attribute_set['tunnel_offset'] = [float(parameters.GetAttributeReal('tunnel_offset')), 'm']

#undercut_attribute_set['vent_east_offset'] = parameters.GetAttributeReal('vent_east_offset')
#undercut_attribute_set['undercut_dev_length'] = parameters.GetAttributeReal('undercut_dev_length')
                                                                              
all_attributes['undercut'] = undercut_attribute_set

parameters = all_children.Query("AdvisorParameterSet", "x.Name.Search('loading')>=0").GetItem(1)
loading_attribute_set['load_elevation'] = [float(parameters.GetAttributeReal("load_elevation")), 'm']
loading_attribute_set['drift_azimuth'] = [round(float(parameters.GetAttributeReal("drift_azimuth") * (180 / math.pi)), 1), 'deg']
loading_attribute_set['minor_pillar'] = [float(parameters.GetAttributeReal('minor_pillar')), 'm']
loading_attribute_set['entry_angle'] = [round(float(parameters.GetAttributeReal('entry_angle') * (180 / math.pi)), 1), 'deg']
loading_attribute_set['minor_offset'] = [float(parameters.GetAttributeReal('minor_offset')), 'm']
loading_attribute_set['west_offset'] = [float(parameters.GetAttributeReal('west_offset')), 'm']

all_attributes['loading'] = loading_attribute_set

totals['loading_dev_length'] = [round(float(parameters.GetAttributeReal('loading_dev_length')), 1), 'm']

all_attributes['totals'] = totals
all_attributes['profile'] = profile

user_name = 'DMH5'
current_date = datetime.date.today()

# Push data into the database
delete_records('DMH5')
insert_parameters(user_name, all_attributes, current_date)

#delete_records('DMH5')
# parameters 'user_name', 'parameters_dict', 'mod_date'
print(get_parameters('user_name', 'DMH5'))
ekl.Notify("Database updated")

