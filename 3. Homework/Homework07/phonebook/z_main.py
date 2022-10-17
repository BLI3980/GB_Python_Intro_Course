import d_html_creator as hc
import e_xml_generator as xg
import a_data_provider as dp

# print(hc.create())
# print(xg.create())

hc.new_create(xg.new_create(dp.data_collection()))
