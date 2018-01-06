"""this is the main part of the assignment"""

# Copyright 2017 Siyuan Tang sytang7@bu.edu
# Copyright 2017 Jia Pei leojia@bu.edu
# Copyright 2017 Xin Li bulixin@bu.edu

import unittest
import subprocess

#please change this to valid author emails
AUTHORS = ['sytang7@bu.edu','leojia@bu.edu','bulixin@bu.edu']

PROGRAM_TO_TEST = "collision.py"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=0.1)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)


class CollisionTestCase(unittest.TestCase):
    "empty class - write this"
    def test_one(self):
        "no error one ball"
        strin = "one 20 10 -2 1"
        correct_out = "3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_two(self):
        "bad input: too many fields on one line"
        strin = "asdfa 10 10 10 10 10"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,1)

    def test_three(self):
        "bad input: invalid numbers"
        strin = "asdfa 10 10 x 10"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,1)

    def test_four(self):
        "Command line problems: not a number"
        time = ["a"]
        strin = "one 20 10 -2 1"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        self.assertEqual(rc,2)

    def test_five(self):
        "Command line problems: Negative time"
        time = ["-2"]
        strin = "one 20 10 -2 1"
        correct_out = "1\none 18 11 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        self.assertEqual(rc,2)
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")

    def test_six(self):
        "Command line problems: no valid number"
        time = []
        strin = "one 20 10 -2 1"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        self.assertEqual(rc,2)

    def test_seven(self):
        "one stand"
        time = ["50"]
        strin = "one 10 20 0 0"
        correct_out = "50\none 10 20 0 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_eight(self):
        "one move"
        time = ["50000"]
        strin = "one 10 20 1 0"
        correct_out = "50000\none 50010 20 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_nine(self):
        "two ball collision"
        time = ["1","3"]
        strin = "one 0 0 1 0\ntwo 15 0 -1 0"
        correct_out = "1\none 1 0 1 0\ntwo 14 0 -1 0\n3\none 2 0 -1 0\ntwo 13 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_ten(self):
        "two ball stand"
        time = ["1","500"]
        strin = "one 0 0 0 0\ntwo 15 15 0 0"
        correct_out = "1\none 0 0 0 0\ntwo 15 15 0 0\n500\none 0 0 0 0\ntwo 15 15 0 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_eleven(self):
        "two move"
        time = ["500"]
        strin = "one 0 0 1 0\ntwo 0 10 1 0"
        correct_out = "500\none 500 0 1 0\ntwo 500 10 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_twelve(self):
        "three ball parallel"
        time = ["3","8","13"]
        strin = "one 0 0 1 0\ntwo 15 0 0 0\nthree 30 0 0 0"
        correct_out = "3\none 3 0 1 0\ntwo 15 0 0 0\nthree 30 0 0 0\n8\none 5 0 0 0\ntwo 18 0 1 0\nthree 30 0 0 0\n13\none 5 0 0 0\ntwo 20 0 0 0\nthree 33 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0) 
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_13(self):
        "four ball parallel"
        time = ["3","8","13","18"]
        strin = "one 0 0 1 0\ntwo 15 0 0 0\nthree 30 0 0 0\nfour 45 0 0 0"
        correct_out = "3\none 3 0 1 0\ntwo 15 0 0 0\nthree 30 0 0 0\nfour 45 0 0 0\n8\none 5 0 0 0\ntwo 18 0 1 0\nthree 30 0 0 0\nfour 45 0 0 0\n13\none 5 0 0 0\ntwo 20 0 0 0\nthree 33 0 1 0\nfour 45 0 0 0\n18\none 5 0 0 0\ntwo 20 0 0 0\nthree 35 0 0 0\nfour 48 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_14(self):
        "five ball parallel"
        time = ["3","8","13","18","23"]
        strin = "one 0 0 1 0\ntwo 15 0 0 0\nthree 30 0 0 0\nfour 45 0 0 0\nfive 60 0 0 0"
        correct_out = "3\none 3 0 1 0\ntwo 15 0 0 0\nthree 30 0 0 0\nfour 45 0 0 0\nfive 60 0 0 0\n8\none 5 0 0 0\ntwo 18 0 1 0\nthree 30 0 0 0\nfour 45 0 0 0\nfive 60 0 0 0\n13\none 5 0 0 0\ntwo 20 0 0 0\nthree 33 0 1 0\nfour 45 0 0 0\nfive 60 0 0 0\n18\none 5 0 0 0\ntwo 20 0 0 0\nthree 35 0 0 0\nfour 48 0 1 0\nfive 60 0 0 0\n23\none 5 0 0 0\ntwo 20 0 0 0\nthree 35 0 0 0\nfour 50 0 0 0\nfive 63 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_15(self):
        "11 ball stand"
        time = ["10"]
        strin = "one 0 0 0 -1\ntwo 15 0 0 0\nthree 30 0 0 0\nfour 45 0 0 0\nfive 60 0 0 0\nsix 75 0 0 0\nseven 90 0 0 0\neight 105 0 0 0\nnine 120 0 0 0\nten 135 0 0 0\neleven 150 0 0 0"
        correct_out = "10\none 0 -10 0 -1\ntwo 15 0 0 0\nthree 30 0 0 0\nfour 45 0 0 0\nfive 60 0 0 0\nsix 75 0 0 0\nseven 90 0 0 0\neight 105 0 0 0\nnine 120 0 0 0\nten 135 0 0 0\neleven 150 0 0 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_16(self):
        "time sequence"
        time = ["50","10","15"]
        strin = "one 10 20 0 0"
        correct_out = "10\none 10 20 0 0\n15\none 10 20 0 0\n50\none 10 20 0 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_17(self):
        time = ["10"]
        strin = "one 0 0 0 0\none 0 0 0 0\none 0 0 0 0"
        correct_out = "10\none 0 0 0 0\none 0 0 0 0\none 0 0 0 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_18(self):
        time = ["10"]
        strin = "one 16 8 -8.62 -9.3\ntwo 0 0 2 1"
        correct_out = "10\none 44.741195 -61.692412 3.5866895 -6.8247474\ntwo -94.941195 -13.307588 -10.20669 -1.4752526\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_19(self):
        time = ["10","50"]
        strin = "one 16 8 -8.6212 -9.1233\ntwo 0 0 2.172 9.11231\nthree -10.172 -10 4 1\nfour 10.12304 0 -12 8.49"
        correct_out = "10\none 11.662157 83.529273 0.43994576 9.3325512\ntwo -119.87356 91.199602 -11.99966 9.1199668\nthree -65.338717 -79.346528 -7.8211724 -8.8560612\nfour 45.009157 -2.5922465 4.9316862 -0.11744675\n50\none 29.259988 456.83132 0.43994576 9.3325512\ntwo -599.85994 455.99827 -11.99966 9.1199668\nthree -378.18561 -433.58898 -7.8211724 -8.8560612\nfour 242.27661 -7.2901163 4.9316862 -0.11744675\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,time,strin)
        out = out.replace(".0000","")
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

def main():
    "show how to use runprogram"
    unittest.main()

if __name__ == '__main__':
    main()

         


