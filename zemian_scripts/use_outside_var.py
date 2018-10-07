class Foo:
    def use_outside_var(self):
        print(f"Outside var root {root}")

root = "test"
Foo().use_outside_var()
