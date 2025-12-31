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

for root in roots:
    joint_chain = get_joint_chain(root)
    joint_chain = joint_chain[:-1]
    previous_control = None
    for jnt in joint_chain:
        base_name = remove_joint_ending(jnt)
        con_name = base_name + "_CON"
        grp_name = base_name + "_GRP"

        con = cmds.circle(
            name=con_name,
            normal=(1, 0, 0),
            radius=3,
            constructionHistory=False
        )[0]

        grp = cmds.group(con, name=grp_name)

        cmds.delete(cmds.parentConstraint(jnt, grp, maintainOffset=False))
        cmds.makeIdentity(con, apply=True, translate=True, rotate=True, scale=True)
        cmds.delete(con, constructionHistory=True)

        cmds.parentConstraint(con, jnt, maintainOffset=True)

        if previous_control:
            cmds.parent(grp, previous_control)

        previous_control = con
