#!/usr/bin/perl
use strict;
use warnings;

# This is a simple Make dependency graph visualizer. It is simple, and
# incomplete. Meant to visualize toy projects only

use feature ':5.10';

say "digraph build {";

my $target        = undef;
my @prerequisites = ();
my $cmd           = "";

my $id_next = 0;
my %node_ids;
my %wrote_edge;

sub node_id
{
    my ($label) = @_;

    if(not exists $node_ids{$label})
    {
        my $id = $id_next++;
        $node_ids{$label} = $id;
        say "node [ label=\"$label\" ] $id";
    }

    return $node_ids{$label};
}

sub write_edge
{
    my ($t,$p,$cmd) = @_;

    my $edge;
    if ($cmd)
    {
        $edge = "$t -> $p [label = \"$cmd\"]";
    }
    else
    {
        $edge = "$t -> $p";
    }

    # suppress duplicates
    return if $wrote_edge{$edge};
    $wrote_edge{$edge} = 1;
    say $edge;
}

sub finish_target
{

    # use Data::Dumper;
    # say("finish:");
    # say Dumper($target);

    if (defined $target)
    {
        for my $p (@prerequisites)
        {
            my $target_id       = node_id($target);
            my $prerequisite_id = node_id($p);

            write_edge(node_id($target),
                       node_id($p),
                       $cmd);
        }

        $target = undef;
        $cmd    = "";
    }
}


while(<>)
{
    next if /^#/;
    next if /^$/;

    if(defined $target)
    {
        if(/^\t(.*)/)
        {
            $cmd .= $1;
            next;
        }

        finish_target();
        # fall through
    }

    if (/^([^\.].+): (.+)/)
    {
        my $prerequisites_scalar;
        ($target, $prerequisites_scalar) = ($1,$2);
        @prerequisites = split(/ /, $prerequisites_scalar);

        # use Data::Dumper;
        # say Dumper($target);
        # say Dumper($prerequisites_scalar);
        # say Dumper(\@prerequisites);

        $cmd = "";
    }
}

finish_target();

say "}";
