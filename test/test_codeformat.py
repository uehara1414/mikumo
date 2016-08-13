import unittest
import os
import pycodestyle


class TestCodeFormat(unittest.TestCase):

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        filelist = []
        for (root, dirs, files) in os.walk("."):
            for name in files:
                if name.endswith(".py"):
                    filelist.append(os.path.join(root, name))

        style = pycodestyle.StyleGuide(quiet=False, ignore=["E5"])

        result = style.check_files(filelist)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == "__main__":
    unittest.main()
