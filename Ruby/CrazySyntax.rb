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

puts 1 == 1.0                                               # true
puts 1.eql?(1.0)                                            # false


# Range : .. vs ...

rng1 = (1..10).to_a                                         # 1 ~ 10
rng2 = (1...10).to_a                                        # 1 ~  9

print rng1, "\n"
print rng2, "\n"


# Array : reverse vs reverse!

arr = [1, 2, 3]

arr.reverse                                                 # not save
print arr, "\n"

arr.reverse!                                                # save
print arr, "\n"


# Symbol : similar with strings but immutable and faster

str = "I"
sym = :U
str += "♥"
# sym += "2"                                                # undefined method `+' for :U:Symbol (NoMethodError)
print str
print sym, "\n"


# .times : an iterator for numbers

10.times do
    print "no"
end
print "\n"


# Return : return the last line's evaluated result without return in UDF

def Say()
    a = "I hate you"
    b = "You make me crazy"
    c = "I want to leave you, but"
    d = "I love you"
end

puts Say()