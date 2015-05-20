import gwy,gwyutils 
import inspect




key = gwy.gwy_app_data_browser_get_current(gwy.APP_DATA_FIELD_KEY)




gr_model = gwy.GraphModel()
cons = gwy.gwy_app_data_browser_get_containers()
# iterate thru containers and datafields
i = 0
for c in cons:
  # get directory of datafields where key is key in container
  #data_view = gwy.gwy_app_data_browser_get_current(gwy.APP_DATA_FIELD)
  dfields = gwyutils.get_data_fields_dir(c)
  for key in dfields.keys():
    data_view = dfields[key]
    #print key
    thickn = 1										# number of lines	
    for nline in range(thickn):								# mean value of several lines to ger profile curve 
      data_line = gwy.DataLine(0,0,False)
      data_view.get_row(data_line, 441 + nline)
      curve = gwy.GraphCurveModel()
      curve.set_data_from_dataline(data_line,0,0)
      s=c.get_string_by_name(key+"/title")
      #curve.props.description=s[len("Immersed "):]				#curve description is full name of the channel excluding "Immersed"
      curve.props.description=s[:] 						#curve description is full name of the channel
      curve.props.mode = 2
      #curve.props.color = gwy.gwy_graph_get_preset_color(1)
      id = gr_model.add_curve(curve)
      print id,gwy.gwy_app_get_graph_key_for_id(id)
  
      #gr_label = gwy.GraphLabel()
      #gr_label.set_model(gr_model)

color = curve.props.color
#gwy_app_get_graph_key_for_id
#print gwy.gwy_app_data_browser_get_current(11)
#print gwy.gwy_app_get_graph_key_for_id(id)
container = gwy.gwy_app_data_browser_get_current(gwy.APP_CONTAINER)
gwy.gwy_app_data_browser_add_graph_model(gr_model, container, True)
#gwy.gwy_process_func_run("profile", container, gwy.RUN_IMMEDIATE)
#print gwy.gwy_container_get_string_by_name(container, "/0/data/title")












