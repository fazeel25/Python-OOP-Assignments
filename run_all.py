import subprocess

files = [
    "assignment1_self.py",
    "assignment2_cls.py",
    "assignment3_public.py",
    "assignment4_classmethod.py",
    "assignment5_static.py",
    "assignment6_constructor_destructor.py",
    "assignment7_access_modifiers.py",
    "assignment8_super.py",
    "assignment9_abstract.py",
    "assignment10_instance_methods.py",
    "assignment11_class_methods.py",
    "assignment12_static_methods.py",
    "assignment13_composition.py",
    "assignment14_aggregation.py",
    "assignment15_mro.py",
    "assignment16_function_decorator.py",
    "assignment17_class_decorator.py",
    "assignment18_property_decorator.py",
    "assignment19_callable.py",
    "assignment20_custom_exception.py",
    "assignment21_iterable.py"
]

for file in files:
    print(f"\nRunning {file}...\n")
    subprocess.run(["python", file])
