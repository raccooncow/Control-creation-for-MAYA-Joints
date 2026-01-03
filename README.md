# Control-creation-for-MAYA-Joints

## Demo
Demo Video: https://youtu.be/7HGAmBfc-8w

## GitHub Repository
GitHub Repo: https://github.com/raccooncow/Control-creation-for-MAYA-Joints.git

## Description
This will be a simple code that creates NURBS Circles and groups, which will be parented to the selected joints, allowing the circles to control the movement of the joints. Copy and paste the code into Maya's script editor, select the joints you want to have controls, and then hit Execute.

### Key Features
NURBS Circles will be created using Python code.
Any circles created will be placed into a group.
The group and circle will be parent-constrained and aligned to the selected joints.
Any history or deforms will be zeroed out.

### Design Considerations
I want to make the circle large, easy to grab, and not hide in the joint chain. I want controls and groups to be parented ONLY if their joints are parented, if there are separate joint chains then my code should create separate control chains, and the control hierarchy should mirror the joint’s parent, not selection order.

### File Structure
Control creation for MAYA Joints.py – Copy and Paste into Maya script editor code.

README.md – Project overview, instructions, and descriptions.