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
    # Create control
    # Create group
    # Align group to joint
    # Zero out control
    # Control drives joint