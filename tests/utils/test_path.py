import unittest
from t3_cicd_cli.utils.path import absolute_path_to_relative


class TestAbsolutePathToRelative(unittest.TestCase):
    def test_local_path(self):
        abs_path = "/Users/JaneDoe/Desktop/project_dir/subdir/file.txt"
        repo = "/Users/JaneDoe/Desktop/project_dir"
        expected = "subdir/file.txt"
        self.assertEqual(absolute_path_to_relative(abs_path, repo), expected)

    def test_git_url(self):
        abs_path = "/Users/JaneDoe/Desktop/example/subdir/file.txt"
        repo = "https://github.com/example.git"
        expected = "subdir/file.txt"
        self.assertEqual(absolute_path_to_relative(abs_path, repo), expected)

    def test_git_url_with_trailing_slash(self):
        abs_path = "/Users/JaneDoe/Desktop/example/subdir/file.txt"
        repo = "https://github.com/example.git/"
        expected = "subdir/file.txt"
        self.assertEqual(absolute_path_to_relative(abs_path, repo), expected)


if __name__ == "__main__":
    unittest.main()
