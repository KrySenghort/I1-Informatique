#=====================================================================================================================================
#==================================================== Chapter 12: Function ===========================================================
#=====================================================================================================================================
# A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better 
# modularity(ម៉ូឌុល ឬ​តម្លៃ) for your application and a high degree of code reusing.
# As we have already known that python give us many built-in functions like print..etc. But we can also create our own functions.
# Those functions are called user-defined functions.

# How to define a function are such that :
         # 1.) Function blocks begin with the keyword def followed by the function name and parentheses(()).
         # 2.) Any input parameters or arguments should be placed within this parentheses(()).
         # 3.) First Statement of a function can be an optional statement-the documentation string of the function or docstring.
         # 4.) The code block within every function start with a colon (:) and is indented.
         # 5.) The statement return [expression] exits a function, optionally passing back an expression to the caller. A return 
         # statement with no arguments is the same as return None.
# Form of Syntax:
                     # def function(parameters):
                     #   'function_docstring'
                     #    function_suite
                     #    return [expression]

#************************** Exercise 1: Introduction
# # Function Definition :
# def printme(str):
#    'This print a passed string into this function.'
#    print(str)
#    return
# # Calling printme function:
# printme('This is the first call to the user defined function!')  # This is the first call to the user defined function!
# printme('Again second call to the same function.')    # Again second call to the same function.

#************************** Exercise 2: Pass by reference Vs value
# def change(mylist):
#    'This change a passed list into this function'
#    print("The values inside the function before change\t:",mylist)
#    mylist[2] = 50
#    print("The values inside the function after change\t:",mylist)
#    return 
# mylist = [10,20,30]
# change(mylist)
# print('The values outside the function is\t\t:',mylist)

# Output:
# The values inside the function before change    : [10, 20, 30]
# The values inside the function after change     : [10, 20, 50]
# The values outside the function is              : [10, 20, 50]

# def changement(list):
#    list[2] = list[1]
#    list[3] = list[4]
#    return 
# list = ['dara','senghort','sreyleak',3,4,5,6]
# print('Before changement element in the list\t\t:',list)
# changement(list)
# print('After changement element in the list\t\t:',list)

# Output:
# Before changement element in the list           : ['dara', 'senghort', 'sreyleak', 3, 4, 5, 6]
# After changement element in the list            : ['dara', 'senghort', 'senghort', 4, 4, 5, 6]

#************************** Exercise 3: Value inside function and Outside of the function
# def changement(mylist):
#    mylist = [1,2,3,4]
#    print('Value inside the function is\t:',mylist)
#    return
# mylist = [10,20,30]
# changement(mylist)
# print('Value outside the function is\t:',mylist)

# Output:
   # Value inside the function is    : [1, 2, 3, 4]
   # Value outside the function is   : [10, 20, 30]

#************************** Exercise 4: Function Arguments
# we can call a function by using the following types of formal arguments such that :
                        # Required arguments
                        # Keyword arguments
                        # Default arguments
                        # Variable length arguments
#===================== Required arguments:
# def name(str):
#    str = 'dara'
#    print(str)
#    return
# name()   # when we call function, we must to clarify the argument such that : name(str) where str is the argument.
#             #     name()
#             # TypeError: name() missing 1 required positional argument: 'str'
#===================== Keyword arguments:
# def name(str):
#    print(str)
#    return
# name(str = 'Senghort')  #   Senghort
# # str = 'Senghort' is the keyword argument that assign value by the user. According above, if we don't assign the value of str then
# # it will not display.

# def printinfo(name,age,sex):
#    print("Name :",name)
#    print("Age  :",age)
#    print("Sex  :",sex)
#    return
# printinfo(name='Senghort',sex='male',age=20)  
# printinfo(name='Senghort',age=20,sex='male')  # we can also reverse the order as you want but we need to show the name of parameter.
# printinfo(sex='male',age=20,name='Senghort')
# # Name : Senghort
# # Age  : 20
# # Sex  : male
# printinfo('Senghort',20,'male')   # if we assign the value of parameters, we have to assign them in the order of each parameter.
# # Name : Senghort
# # Age  : 20
# # Sex  : male
#====================== Default arguments:
# def printinfo(name,age=35):
#    print('Name :',name)
#    print('Age  :',age)
# printinfo(age=50,name='Senghort')   # this is overwrite method that age before will update to the new one.
# # Name : Senghort
# # Age  : 50 
# printinfo(name='Kry')
# # Name : Kry
# # Age  : 35
#====================== Variable-Length arguments: when we need to process a function for more arguments than we specified while
# # defining the function. These arguments are called variable-length arguments and are not name in the function definition, unlike 
# # required and default arguments.
# def printinfo(arg1,*vartuple):
# # an asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments. This tuple remains 
# # empty if no additional arguments are specified during the function call.
#    print("Output is :%s" %arg1)  # 10  70  1
#    for var in vartuple:
#       print(var)  #  60  50  2  4  5  6  7  7  8  8   
# printinfo(10)
# printinfo(70,60,50)
# printinfo(1,2,4,5,6,7,7,8,8)

# def name(a,*x):
#       print('%s'%a,end=',')
#       # for var in x:        when we comment on this line it will display : 2,(5,),3,(4, 5, 6, 7, 8, 9),Senghort,('rase',),
#       print(x,end=',')
# name(2,5)
# name(3,4,5,6,7,8,9)
# name('Senghort','rase')
# # Output:
#                         # 2,5,3,4,5,6,7,8,9,Senghort,rase,

#************************** Exercise 5: Anonymous Functions is the function that are not declared in the standard manner by using the 
# def keyword. We can use the lambda keyword to create small anonymous functions.
      # 1.) Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain 
      #     commands or multiple expressions.
      # 2.) An anonymous function cannot be a direct call to print because lambda requires an expression.
      # 3.) Lambda functions have their own local namespace and cannot access other variables than those in their parameter list and 
      #     those in global namespace.
      # 4.) Although it appears that lambdas are a one-line version of a function, they are not equivalent to inline statements in C
      #     or C++, whose purpose is to stack allocation by passing function, during invocation for performance reasons.
# from math import sqrt
# arg1 = input('Enter arg1 : ')
# arg2 = input('Enter arg2 : ')
# arg3 = int(input('Enter arg3 : '))

# sum = lambda arg1, arg2: arg1 + arg2
# print("Sum of these two args is :",sum(int(arg1),int(arg2)))
# sum = lambda arg1,arg2,arg3: arg1 + arg2 + arg3
# print("Sum of these three args is :",sum(int(arg1),int(arg2),arg3))

# substraction = lambda arg1,arg2: arg1-arg2
# print("rest value is :",substraction(int(arg1),int(arg2)))
# substraction = lambda arg1,arg2,arg3: arg1-arg2-arg3
# print("rest value is :",substraction(int(arg1),int(arg2),arg3))

# multiply = lambda arg1,arg2,arg3: arg1*arg2*arg3
# print("Multiply between x, y and z is :",multiply(int(arg1),int(arg2),arg3))

# division = lambda arg1,arg2,arg3: arg1/arg2/arg3
# print('Division between a b and c is: ',division(int(arg1),int(arg2),arg3))

# srt = lambda arg1,arg2: sqrt(arg1**2 + arg2**2)
# print("square root of a^2 + b^2 is :",srt(int(arg1),int(arg2)))
# cubrt = lambda arg1,arg2,arg3: pow((arg1**3 + arg2**3 + arg3**3),1/3)
# print("cube root of x^3 + y^3 + z^3 is :",cubrt(int(arg1),int(arg2),arg3))

# remainder = lambda arg1,arg2,arg3: arg1 % arg2 % arg3
# print('remainder of these three number is : ',remainder(int(arg1),int(arg2),arg3))
# # Output:
                        # Enter arg1 : 12
                        # Enter arg2 : 5
                        # Enter arg3 : 6
                        # Sum of these two args is : 17
                        # Sum of these three args is : 23
                        # rest value is : 7
                        # rest value is : 1
                        # Multiply between x, y and z is : 360
                        # Division between a b and c is:  0.39999999999999997
                        # square root of a^2 + b^2 is : 13.0
                        # cube root of x^3 + y^3 + z^3 is : 12.742466394033986
                        # remainder of these three number is :  2

#************************** Exercise 6: Return Statement
# def sum(arg1,arg2):
#       total = arg1+arg2
#       print('Inside the function is :',total)
#       return total
# a = int(input('Enter a : '))
# b = int(input('Enter b : '))
# total = sum(a,b)
# print('Outside the function is :',total)
# # Output:
                        # Enter a : 12
                        # Enter b : 45
                        # Inside the function is : 57 
                        # Outside the function is : 57   if we don't have return statement it will display None.

#************************** Exercise 7: Summation inside and outside of function that mention on local variable and global variable.
# def sum(a,b):
#       total = a+b
#       print('Summation a and b is :',total)
#       return total
# sum(3,4)
# print('Summation a and b is :',total)  # because total has no value or not assign the value.
#       # Summation a and b is : 7
#       # Traceback (most recent call last):
#       #   File "d:\Year 01\Informatique\Basic to Advance Python\Basic Python\Chapter_12_Function.py", line 210, in <module>
#       #     print('Summation a and b is :',total)
#       # NameError: name 'total' is not defined

#************************** Exercise 8: Fibonacci number module
# def fibonacci(n):
#       result = []
#       a = 0
#       b = 1
#       while b<n:
#             result.append(b)
#             a, b = b ,a+b
#       return result
# x = int(input('Enter number of fibonacci sequence :'))
# y = fibonacci(x)
# print(y)
#                   # Enter number of fibonacci sequence :2022
#                   # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

# def fib(n):
#       result = []
#       a = 0
#       b = 1
#       while b<n:
#             result.append(b)
#             a = b
#             b +=a
#       return result
# a = int(input('Enter number of fibonacci sequence :'))
# y = fib(a)
# print(y)
#                   # Enter number of fibonacci sequence :2022
#                   # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

#************************** Exercise 9: Namespaces and Scopping
# Money = 2000
# def addMoney(Money):
#       Money = Money + 2022
#       return Money
# print(Money)     # 2000
# total = addMoney(Money)
# print(total)     # 4022

#************************** Exercise 10: dir() function is used to returns a sorted list of strings containing the names defined by
# a module. This list contains the names of all the modules, variables and functions that are defined as a module.

# import math
# content = dir(math)
# print(content)
# #  ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 
# #  'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor',
# #  'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma'
# #  , 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh',
# #  'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

# import numpy
# content = dir(numpy)
# print(content)

# ['ALLOW_THREADS', 'AxisError', 'BUFSIZE', 'CLIP', 'ComplexWarning', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_IGNORE', 'ERR_LOG'
# ,'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN', 'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID', 'FPE_OVERFLOW', 'FPE_UNDERFLOW'
# , 'False_', 'Inf', 'Infinity', 'MAXDIMS', 'MAY_SHARE_BOUNDS', 'MAY_SHARE_EXACT', 'ModuleDeprecationWarning', 'NAN', 'NINF', 'NZERO', 'NaN', 'PINF', 'PZERO', 'RAISE', 'RankWarning', 'SHIFT_DIVIDEBYZERO', 'SHIFT_INVALID', 'SHIFT_OVERFLOW', 'SHIFT_UNDERFLOW', 'ScalarType', 'Tester', 'TooHardError', 'True_', 'UFUNC_BUFSIZE_DEFAULT', 'UFUNC_PYVALS_NAME', 'VisibleDeprecationWarning', 'WRAP', '_CopyMode', '_NoValue', '_UFUNC_API', '__NUMPY_SETUP__', '__all__', '__builtins__', '__cached__', '__config__', '__deprecated_attrs__', '__dir__', '__doc__', '__expired_functions__', '__file__', '__getattr__', '__git_version__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_add_newdoc_ufunc', '_distributor_init', '_financial_names', '_globals', '_mat', '_pyinstaller_hooks_dir', '_pytesttester', '_version', 'abs', 'absolute', 'add', 'add_docstring', 'add_newdoc', 'add_newdoc_ufunc', 'all', 'allclose', 'alltrue', 'amax', 'amin', 'angle', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argpartition', 'argsort', 'argwhere', 'around', 'array', 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'asanyarray', 'asarray', 'asarray_chkfinite', 'ascontiguousarray', 'asfarray', 'asfortranarray', 'asmatrix', 'atleast_1d', 'atleast_2d', 'atleast_3d', 'average', 'bartlett', 'base_repr', 'binary_repr', 'bincount', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'blackman', 'block', 'bmat', 'bool8', 'bool_', 'broadcast', 'broadcast_arrays', 'broadcast_shapes', 'broadcast_to', 'busday_count', 'busday_offset', 
# 'busdaycalendar', 'byte', 'byte_bounds', 'bytes0', 'bytes_', 'c_', 'can_cast', 'cast', 'cbrt', 'cdouble', 'ceil', 'cfloat', 'char', 
# 'character', 'chararray', 'choose', 'clip', 'clongdouble', 'clongfloat', 'column_stack', 'common_type', 'compare_chararrays', 
# 'compat', 'complex128', 'complex64', 'complex_', 'complexfloating', 'compress', 'concatenate', 'conj', 'conjugate', 'convolve', 
# 'copy', 'copysign', 'copyto', 'core', 'corrcoef', 'correlate', 'cos', 'cosh', 'count_nonzero', 'cov', 'cross', 'csingle', 
# 'ctypeslib', 'cumprod', 'cumproduct', 'cumsum', 'datetime64', 'datetime_as_string', 'datetime_data', 'deg2rad', 'degrees', 'delete'
# , 'deprecate', 'deprecate_with_doc', 'diag', 'diag_indices','diag_indices_from', 'diagflat', 'diagonal', 'diff', 'digitize', 'disp',
# 'divide', 'divmod', 'dot', 'double', 'dsplit', 'dstack', 'dtype', 'e', 'ediff1d', 'einsum', 'einsum_path', 'emath', 'empty', 
# 'empty_like', 'equal', 'errstate', 'euler_gamma', 'exp', 'exp2', 'expand_dims', 'expm1', 'extract', 'eye', 'fabs', 
# 'fastCopyAndTranspose', 'fft', 'fill_diagonal', 'find_common_type', 'finfo', 'fix', 'flatiter', 'flatnonzero', 'flexible', 'flip', 
# 'fliplr', 'flipud', 'float16', 'float32', 'float64', 'float_', 'float_power', 'floating', 'floor', 'floor_divide', 'fmax', 'fmin', 
# 'fmod', 'format_float_positional', 'format_float_scientific', 'format_parser', 'frexp', 'from_dlpack', 'frombuffer', 'fromfile', 
# 'fromfunction', 'fromiter', 'frompyfunc', 'fromregex', 'fromstring', 'full', 'full_like', 'gcd', 'generic', 'genfromtxt', 
# 'geomspace', 'get_array_wrap', 'get_include', 'get_printoptions', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj', 'gradient', 
# 'greater', 'greater_equal', 'half', 'hamming', 'hanning', 'heaviside', 'histogram', 'histogram2d', 'histogram_bin_edges', 
# 'histogramdd', 'hsplit', 'hstack', 'hypot', 'i0', 'identity', 'iinfo', 'imag', 'in1d', 'index_exp', 'indices', 'inexact', 'inf', 
# 'info', 'infty', 'inner', 'insert', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_', 'intc', 'integer', 'interp', 'intersect1d', 
# 'intp', 'invert', 'is_busday', 'isclose', 'iscomplex', 'iscomplexobj', 'isfinite', 'isfortran', 'isin', 'isinf', 'isnan', 'isnat', 
# 'isneginf', 'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issctype', 'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 
# 'ix_', 'kaiser', 'kron', 'lcm', 'ldexp', 'left_shift', 'less', 'less_equal', 'lexsort', 'lib', 'linalg', 'linspace', 
# 'little_endian', 'load', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logaddexp', 'logaddexp2', 'logical_and', 'logical_not', 
# 'logical_or', 'logical_xor', 'logspace', 'longcomplex', 'longdouble', 'longfloat', 'longlong', 'lookfor', 'ma', 'mask_indices', 
# 'mat', 'math', 'matmul', 'matrix', 'matrixlib', 'max', 'maximum', 'maximum_sctype', 'may_share_memory', 'mean', 'median', 'memmap',
# 'meshgrid', 'mgrid', 'min', 'min_scalar_type', 'minimum', 'mintypecode', 'mod', 'modf', 'moveaxis', 'msort', 'multiply', 'nan', 
# 'nan_to_num', 'nanargmax', 'nanargmin', 'nancumprod', 'nancumsum', 'nanmax', 'nanmean', 'nanmedian', 'nanmin', 'nanpercentile', 
# 'nanprod', 'nanquantile','nanstd', 'nansum', 'nanvar', 'nbytes', 'ndarray', 'ndenumerate', 'ndim', 'ndindex', 'nditer', 'negative',
# 'nested_iters', 'newaxis', 'nextafter', 'nonzero', 'not_equal', 'numarray', 'number', 'obj2sctype', 'object0', 'object_', 'ogrid',
# 'oldnumeric', 'ones', 'ones_like', 'os', 'outer', 'packbits', 'pad', 'partition', 'percentile', 'pi', 'piecewise', 'place', 'poly', 
# 'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polynomial', 'polysub', 'polyval', 'positive', 'power'
# , 'printoptions', 'prod', 'product', 'promote_types', 'ptp', 'put', 'put_along_axis', 'putmask', 'quantile', 'r_', 'rad2deg', 
# 'radians', 'random', 'ravel', 'ravel_multi_index', 'real', 'real_if_close', 'rec', 'recarray', 'recfromcsv', 'recfromtxt', 
# 'reciprocal', 'record', 'remainder', 'repeat', 'require', 'reshape', 'resize', 'result_type', 'right_shift', 'rint', 'roll', 
# 'rollaxis', 'roots', 'rot90', 'round', 'round_', 'row_stack', 's_', 'safe_eval', 'save', 'savetxt', 'savez', 'savez_compressed', 
# 'sctype2char', 'sctypeDict', 'sctypes', 'searchsorted', 'select', 'set_numeric_ops', 'set_printoptions', 'set_string_function', 
# 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'seterrobj', 'setxor1d', 'shape', 'shares_memory', 'short', 'show_config', 
# 'sign', 'signbit', 'signedinteger', 'sin', 'sinc', 'single', 'singlecomplex', 'sinh', 'size', 'sometrue', 'sort', 'sort_complex', 
# 'source', 'spacing', 'split', 'sqrt', 'square', 'squeeze', 'stack', 'std', 'str0', 'str_', 'string_', 'subtract', 'sum', 'swapaxes'
# , 'sys', 'take', 'take_along_axis', 'tan', 'tanh', 'tensordot', 'test', 'testing', 'tile', 'timedelta64', 'trace', 
# 'tracemalloc_domain', 'transpose', 'trapz', 'tri', 'tril', 'tril_indices', 'tril_indices_from', 'trim_zeros', 'triu', 
# 'triu_indices', 'triu_indices_from', 'true_divide', 'trunc', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 
# 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode_', 'union1d', 'unique', 'unpackbits', 'unravel_index', 
# 'unsignedinteger', 'unwrap', 'use_hugepage', 'ushort', 'vander', 'var', 'vdot', 'vectorize','version', 'void', 'void0', 'vsplit', 
# 'vstack', 'warnings', 'where', 'who', 'zeros', 'zeros_like']

# import matplotlib
# content = dir(matplotlib)
# print(content)
# ['ExecutableNotFoundError', 'MatplotlibDeprecationWarning', 'MutableMapping', 'Parameter', 'Path', 'RcParams', '_ExecInfo', 
# '_VersionInfo','__bibtex__', '__builtins__', '__cached__', '__doc__', '__file__', '__getattr__', '__loader__', '__name__', 
# '__package__', '__path__', '__spec__', '_add_data_doc', '_api', '_c_internal_utils', '_check_versions', '_cm', '_cm_listed', 
# '_color_data', '_deprecated_ignore_map', '_deprecated_map', '_deprecated_remain_as_none', '_docstring', '_ensure_handler', 
# '_enums', '_fontconfig_pattern', '_get_config_or_cache_dir', '_get_executable_info', '_get_ssl_context', '_get_version', 
# '_get_xdg_cache_dir', '_get_xdg_config_dir', '_init_tests', '_label_from_arg', '_log', '_logged_cached', '_open_file_or_url', 
# '_parse_to_version_info', '_path', '_preprocess_data', '_rc_params_in_file', '_replacer', '_version', 'atexit', 'bezier', 'cbook', 
# 'checkdep_usetex', 'cm', 'color_sequences', 'colormaps', 'colors', 'contextlib', 'cycler', 'defaultParams', 'default_test_modules'
# , 'ft2font', 'functools', 'get_backend', 'get_cachedir', 'get_configdir', 'get_data_path', 'importlib', 'inspect', 'interactive'
# , 'is_interactive', 'is_url', 'locale', 'logging', 'matplotlib_fname', 'namedtuple', 'numpy', 'os', 'parse_version', 'path', 
# 'pprint', 'rc', 'rcParams', 'rcParamsDefault', 'rcParamsOrig', 'rc_context', 'rc_file', 'rc_file_defaults', 'rc_params', 
# 'rc_params_from_file', 'rcdefaults', 'rcsetup', 're', 'sanitize_sequence', 'scale', 'set_loglevel', 'shutil', 'subprocess', 'sys', 
# 'tempfile', 'test', 'ticker', 'transforms', 'use', 'validate_backend', 'warnings']


# import string
# content = dir(string)
# print(content)
# # ['Formatter', 'Template', '_ChainMap', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
# # '__package__', '__spec__', '_re', '_sentinel_dict', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords',
# # 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']

# import time
# content = dir(time)
# print(content)
# # ['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'ctime', 'daylight', 
# # 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time',
# # 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone',
# # 'tzname']

# import functools
# content = dir(functools)
# print(content)
# # ['GenericAlias', 'RLock', 'WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', '_CacheInfo', '_HashedSeq', '_NOT_FOUND', '__all__', 
# # '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_c3_merge', '_c3_mro', 
# # '_compose_mro', '_convert', '_find_impl', '_ge_from_gt', '_ge_from_le', '_ge_from_lt', '_gt_from_ge', '_gt_from_le', '_gt_from_lt'
# # , '_initial_missing', '_le_from_ge', '_le_from_gt', '_le_from_lt', '_lru_cache_wrapper', '_lt_from_ge', '_lt_from_gt', 
# # '_lt_from_le', '_make_key', '_unwrap_partial', 'cache', 'cached_property', 'cmp_to_key', 'get_cache_token', 'lru_cache', 
# # 'namedtuple', 'partial', 'partialmethod', 'recursive_repr', 'reduce', 'singledispatch', 'singledispatchmethod', 'total_ordering', 
# # 'update_wrapper', 'wraps']

#************************** Exercise 11: Reload Function








#************************** Exercise 12:







#************************** Exercise 13:








#************************** Exercise 14:







#************************** Exercise 15:









#************************** Exercise 16:









#************************** Exercise 17:








#************************** Exercise 18:







#************************** Exercise 19:










#************************** Exercise 20:










#************************** Exercise 21:







#************************** Exercise 22:










#************************** Exercise 23:










#************************** Exercise 24:








#************************** Exercise 25:





#************************** Exercise 26:







#************************** Exercise 27:
