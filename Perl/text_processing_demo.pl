#!/usr/bin/perl
use strict;
use warnings;

=pod
=head1 NAME
text_processing_demo.pl - Simple Perl text processing demo

=head1 DATE
2025.10.20.

=head1 DESCRIPTION
Shows regex substitution, array/hash handling, map/grep usage,
and simple list transformations. File I/O code is commented out.
=cut

# Simple Perl demo: regex, array/hash, map/grep, list ops

# 1. Regex replace
my $text = "Perl is powerful, flexible, and quirky!";
$text =~ s/powerful/versatile/;
print "1. After substitution: $text\n";

# 2. Count word frequency
my @words = split(/\s+/, $text);
my %count;
$count{$_}++ for @words;

print "\n2. Word frequencies:\n";
foreach my $word (sort keys %count) {
    print "\t$word => $count{$word}\n";
}

# 3. Filter long words (>4 chars)
my @long_words = grep { length($_) > 4 } @words;
print "\n3. Long words: @long_words\n";

# 4. File input example (disabled)
# open(my $fh, '<', 'example.txt') or die $!;
# while (<$fh>) { print if /Perl/; }
# close $fh;

# 5. Uppercase all words
my @upper = map { uc($_) } @words;
print "\n5. Uppercased words: @upper\n";
