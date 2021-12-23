import importlib.util as imu

core_a_spec = imu.spec_from_file_location('core', 'a/core.cpython-39-x86_64-linux-gnu.so')
core_a = imu.module_from_spec(core_a_spec)
core_a_spec.loader.exec_module(core_a)

# Hello
print(core_a.get())

core_b_spec = imu.spec_from_file_location('core', 'b/core.cpython-39-x86_64-linux-gnu.so')
core_b = imu.module_from_spec(core_b_spec)
core_b_spec.loader.exec_module(core_b)

# World
print(core_b.get())

# Hello
print(core_a.get())

