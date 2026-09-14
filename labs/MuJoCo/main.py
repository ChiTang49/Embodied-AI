import os
import time

import mujoco
import mujoco.viewer
import ikpy.chain
import transforms3d as tf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'universal_robots_ur5e', 'scene.xml')
URDF_PATH = os.path.join(BASE_DIR, 'model', 'ur5e.urdf')

def main():
    model = mujoco.MjModel.from_xml_path(MODEL_PATH)
    data = mujoco.MjData(model)

    my_chain = ikpy.chain.Chain.from_urdf_file(URDF_PATH, active_links_mask=[False, False] + [True] * 6 + [False])
 
    ee_pos = [-0.13, 0.5, 0.1]
    ee_euler = [3.14, 0, 1.57]
    ref_pos = [0, 0, -1.57, -1.34, 2.65, -1.3, 1.55, 0, 0]
    ee_orientation = tf.euler.euler2mat(*ee_euler)

    joint_angles = my_chain.inverse_kinematics(ee_pos, ee_orientation, "all", initial_position=ref_pos)
    ctrl = joint_angles[2:8]
    data.ctrl[:6] = ctrl
 
    with mujoco.viewer.launch_passive(model, data) as viewer:
        while viewer.is_running():
            data.ctrl[:6] = ctrl
            mujoco.mj_step(model, data)
            viewer.sync()
            time.sleep(0.002)
 
if __name__ == "__main__":
    main()