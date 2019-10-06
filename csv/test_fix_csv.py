import unittest
import sys
import os

from textwrap import dedent
from contextlib import contextmanager, redirect_stdout
from io import StringIO
from importlib.machinery import SourceFileLoader
from tempfile import NamedTemporaryFile


class FixCSVTests(unittest.TestCase):
    """Tests for fix_csv.py."""

    maxDiff = None

    def test_pipe_file_to_csv_file(self):
        old_contents = dedent("""
            2012|Lexus|LFA
            2009|GMC|Yukon XL 1500
            1965|Ford|Mustang
            2005|Hyundai|Sonata
            1995|Mercedes-Benz|C-Class
        """).lstrip()
        expected = dedent("""
            2012,Lexus,LFA
            2009,GMC,Yukon XL 1500
            1965,Ford,Mustang
            2005,Hyundai,Sonata
            1995,Mercedes-Benz,C-Class
        """).lstrip()
        with make_file(old_contents) as old, make_file("") as new:
            output = run_program("fix_csv.py", args=[old, new])
            with open(new) as new_file:
                new_contents = new_file.read()
        self.assertEqual(expected, new_contents)
        self.assertEqual("", output)

    def test_delimiter_in_output(self):
        old_contents = dedent("""
            02|Waylon Jennings|Honky Tonk Heroes (Like Me)
            04|Kris Kristofferson|To Beat The Devil
            11|Johnny Cash|Folsom Prison Blues
            13|Billy Joe Shaver|Low Down Freedom
            21|Hank Williams III|Mississippi Mud
            22|David Allan Coe|Willie, Waylon, And Me
            24|Bob Dylan|House Of The Risin' Sun
        """).lstrip()
        expected = dedent("""
            02,Waylon Jennings,Honky Tonk Heroes (Like Me)
            04,Kris Kristofferson,To Beat The Devil
            11,Johnny Cash,Folsom Prison Blues
            13,Billy Joe Shaver,Low Down Freedom
            21,Hank Williams III,Mississippi Mud
            22,David Allan Coe,"Willie, Waylon, And Me"
            24,Bob Dylan,House Of The Risin' Sun
        """).lstrip()
        with make_file(old_contents) as old, make_file("") as new:
            output = run_program("fix_csv.py", args=[old, new])
            with open(new) as new_file:
                new_contents = new_file.read()
        self.assertEqual(expected, new_contents)
        self.assertEqual("", output)

    def test_original_file_is_unchanged(self):
        old_contents = dedent("""
            2012|Lexus|LFA
            2009|GMC|Yukon XL 1500
        """).lstrip()
        with make_file(old_contents) as old, make_file("") as new:
            run_program("fix_csv.py", args=[old, new])
            with open(old) as old_file:
                contents = old_file.read()
        self.assertEqual(old_contents, contents)

    def test_call_with_too_many_files(self):
        with make_file("") as old, make_file("") as new:
            with self.assertRaises(BaseException):
                run_program("fix_csv.py", args=[old, new, old])


class DummyException(Exception):
    """No code will ever raise this exception."""


def run_program(path, args=[], raises=DummyException):
    """
    Run program at given path with given arguments.

    If raises is specified, ensure the given exception is raised.
    """
    old_args = sys.argv

    assert all(isinstance(a, str) for a in args)

    try:
        sys.argv = [path] + args
        with redirect_stdout(StringIO()) as output:
            try:
                if "__main__" in sys.modules:
                    del sys.modules["__main__"]
                SourceFileLoader("__main__", path).load_module()
            except raises:
                return output.getvalue()
            except SystemExit as e:
                if e.args != (0,):
                    raise
            if raises is not DummyException:
                raise AssertionError(f"{raises} not raised")
            return output.getvalue()
    finally:
        sys.argv = old_args


@contextmanager
def make_file(contents=None):
    """Context manager providing name of a file containing given contents."""
    with NamedTemporaryFile(mode="wt", encoding="utf-8", delete=False) as f:
        if contents:
            f.write(contents)
    try:
        yield f.name
    finally:
        os.remove(f.name)


if __name__ == '__main__':
    unittest.main(verbosity=2)
