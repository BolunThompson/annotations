from datatypes.Arg import make_arg_simple
from datatypes.Operand import Operand

import AnnotationGeneration
from parallelizers.Parallelizer import Parallelizer

cmd_name = "head"

# TODO: does head take head of each file? then IF possible; same for tail


def test_head_1():
    args = [make_arg_simple(["-q"])]
    operands = [Operand("in1.txt"),
                Operand("in2.txt")]

    meta = AnnotationGeneration.get_meta_from_cmd_invocation(cmd_name, args, operands)

    assert len(meta.get_input_list()) == 2
    assert len(meta.get_output_list()) == 2     # stdout and stderr

    assert len(meta.get_parallelizer_list()) == 1
    [parallelizer1] = meta.get_parallelizer_list()
    assert parallelizer1 == Parallelizer.make_parallelizer_indiv_files()


def test_head_2():
    args = [make_arg_simple(["--version"])]
    operands = [Operand("in1.txt"),
                Operand("-"),
                Operand("in2.txt")]

    meta = AnnotationGeneration.get_meta_from_cmd_invocation(cmd_name, args, operands)

    assert len(meta.get_input_list()) == 3
    assert len(meta.get_output_list()) == 2

    assert len(meta.get_parallelizer_list()) == 1
    [parallelizer1] = meta.get_parallelizer_list()
    assert parallelizer1 == Parallelizer.make_parallelizer_indiv_files()
