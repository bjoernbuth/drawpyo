# %%

from pathlib import Path

# %%
import drawpyo
from drawpyo.diagram_types import TreeDiagram


file_path = Path(__file__).parent

tree = TreeDiagram(
    file_path=file_path,
    file_name="Tree Name.drawio",
)

# %%
from drawpyo.diagram_types import NodeObject

# Top object
grinders = NodeObject(
    tree=tree, value="Appliances for Grinding Coffee", base_style="rounded rectangle"
)

# Main categories
blade_grinders = NodeObject(tree=tree, value="Blade Grinders", parent=grinders)
burr_grinders = NodeObject(tree=tree, value="Burr Grinders", parent=grinders)
blunt_objects = NodeObject(tree=tree, value="Blunt Objects", parent=grinders)

# %%
# Other
elec_blade = NodeObject(tree=tree, value="Electric Blade Grinder", parent=blade_grinders)
mnp = NodeObject(tree=tree, value="Mortar and Pestle", parent=blunt_objects)

# Conical Burrs
conical = NodeObject(tree=tree, value="Conical Burrs", parent=burr_grinders)
elec_conical = NodeObject(tree=tree, value="Electric", parent=conical)
manual_conical = NodeObject(tree=tree, value="Manual", parent=conical)

# %%
base_obj = drawpyo.diagram.Object(page=page)

# %%
tree.auto_layout()
tree.write()

# %%
