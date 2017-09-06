# The function 'hiera_include' is deprecated in favor of using 'lookup'
# The hiera, hiera_array, hiera_hash, and hiera_include functions
# are all deprecated, and will be removed in Puppet 6.
hiera_include('classes')
#
# 'lookup'
# Do a unique merge lookup of class names,
# then add all of those classes to the catalog (like hiera_include):
# lookup('classes', Array[String], 'unique').include
