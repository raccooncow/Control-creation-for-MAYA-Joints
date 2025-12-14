# Add imports
import maya.cmds as cmds

# Get selected Joints
joints = cmds.ls(selection=True, type="joint")

# Create empty dict to store joint
joint_ctrl_map = {}
# Function remove_joint_ending(name)
def remove_joint_ending(name):
    # For loop for joints ending in JNT or jnt
    for ending in ["_JNT", "_jnt"]:
        # If joint ends with either
        if name.endswith(ending):
            # Remove ending and return name
            return name[:-len(ending)]
    # If no ending, return og name
    return name

# Create controls & groups
for jnt in joints:
    base_name = remove_joint_ending(jnt)
    con_name = base_name + "_CON"
    grp_name = base_name + "_GRP"
    # Create control
    con = cmds.circle(
        name = con_name,
        normal = (1, 0, 0),
        radius = 3,
        constructionHistory=False
    )[0]
    # Create group
    grp = cmds.group(con, name=grp_name)
    # Align group to joint
    cmds.delete(cmds.parentConstraint(jnt, grp, maintainOffset=False))
    # Zero out control

    # Control drives joint
