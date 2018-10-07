def foo():
    raise Exception('failed on purpose.')


try:
    foo()
except Exception as e:
    print(e)
    print(type(e))
    print("We caught an exception here:")
    import sys, traceback
    tb = sys.exc_info()[2]
    tb_str = traceback.format_tb(tb)
    print(tb_str)
    print("Exception ended.")
print("Program exit normal.")

print("New python 3.2.3+ exception style has traceback attr")
try:
    foo()
except Exception as e:
    print(traceback.format_tb(e.__traceback__))
print("Done.")