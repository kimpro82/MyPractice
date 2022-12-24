# Ruby's crazy syntax

# 2022.12.24 (It is a good day to code!)


# Falsey 0

if 0 == false
    puts "0 is false."
elsif 0 == true
    puts "0 is true, surprisingly."
else
    puts "0 is neither false nor true but falsey."
end


# Comparison operator vs eql?

puts 1 == 1.0                                       # true
puts 1.eql?(1.0)                                    # false


# Range : .. vs ...

rng1 = (1..10).to_a                                 # 1 ~ 10
rng2 = (1...10).to_a                                # 1 ~  9

print rng1, "\n"
print rng2, "\n"


# Array : reverse vs reverse!

arr = [1, 2, 3]

arr.reverse
print arr, "\n"

arr.reverse!
print arr, "\n"


# Symbol : similar with Hash but immutable (and faster)
# .times : an iterator for numbers
# UDF : return without return