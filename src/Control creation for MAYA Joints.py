import maya.cmds as cmds

roots = cmds.ls(selection=True, type="joint")

joint_ctrl_map = {}
def remove_joint_ending(name):
    for ending in ["_JNT", "_jnt"]:
        if name.endswith(ending):
            return name[:-len(ending)]
    return name

def get_joint_chain(root):
    chain = [root]
    current = root

    while True:
        children = cmds.listRelatives(current, children=True, type="joint") or []
        if not children:
            break
        current = children[0]
        chain.append(current)

    return chain

for jnt in joints:
    base_name = remove_joint_ending(jnt)
    con_name = base_name + "_CON"
    grp_name = base_name + "_GRP"
    con = cmds.circle(
        name = con_name,
        normal = (1, 0, 0),
        radius = 3,
        constructionHistory=False
    )[0]
    grp = cmds.group(con, name=grp_name)
    cmds.delete(cmds.parentConstraint(jnt, grp, maintainOffset=False))
    cmds.makeIdentity(con, apply=True, translate=True, rotate=True, scale=True)
    cmds.delete(con, constructionHistory=True)
    cmds.parentConstraint(con, jnt, maintainOffset=True)
    joint_ctrl_map[jnt] = {
        "con": con,
        "grp": grp
    }

for jnt in joints:
    parent_joint = cmds.listRelatives(jnt, parent=True, type="joint")
    if parent_joint:
        parent_joint = parent_joint[0]
        if parent_joint in joint_ctrl_map:
            cmds.parent(
                joint_ctrl_map[jnt]["grp"],
                joint_ctrl_map[parent_joint]["con"]
            )