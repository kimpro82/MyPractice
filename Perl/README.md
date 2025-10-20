# [My Perl Practice](../README.md#my-perl--practice)


### **\<References>**

- [www.perl.org](https://www.perl.org/)
- [JDoodle / Perl Online Compiler](https://www.jdoodle.com/execute-perl-online)


### **\<List>**

- [Initial Practice : Text Processing Demo (2025.10.20)](#initial-practice--text-processing-demo-20251020)


## [Initial Practice : Text Processing Demo (2025.10.20)](#list)

- Simple Perl demo: regex, array/hash, map/grep, list ops

### Code and Results
<details>
  <summary>Code : text_processing_demo.pl</summary>

  ```perl
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
  ```
</details>
<details>
  <summary>Results</summary>

  ```txt
  1. After substitution: Perl is versatile, flexible, and quirky!

  2. Word frequencies:
    Perl => 1
    and => 1
    flexible, => 1
    is => 1
    quirky! => 1
    versatile, => 1

  3. Long words: versatile, flexible, quirky!

  5. Uppercased words: PERL IS VERSATILE, FLEXIBLE, AND QUIRKY!
  ```
</details>
