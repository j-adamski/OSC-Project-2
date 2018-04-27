import unittest
import t3
import json
from unittest.mock import patch
import builtins

class TestT3(unittest.TestCase):
    
    def test_t3Complete(self):
        inputFile = 'tasks/tasks.json'
        jsonData = open(inputFile).read()
        data = json.loads(jsonData)

        t3.t3Complete("homework3")

        for k in data:
            if "homework3" == k['projectName']:
                self.assertTrue(k['completed'])

        
    def test_t3Report(self):
        t3.t3Report("active")
        t3.t3Report("completed")
        t3.t3Report("all")
        t3.t3Report("invalid option")

        
    def test_t3Add(self):
        t3.t3Add("test project")

    def test_t3Delete(self):
        t3.t3Delete("test project")

    def test_t3Edit(self):
        with patch.object(builtins, 'input', lambda newTime: 1.1266946):
            t3.t3Edit("homework3")

        with patch.object(builtins, 'input', lambda newTime: 'ff'):
            self.assertRaises(ValueError, t3.t3Edit, "homework3")

        with patch.object(builtins, 'input', lambda newTime: 1.55):
            t3.t3Edit("invalid project")

    def test_t3Start(self):
        t3.t3Start("homework3")

    def test_t3Stop(self):
        t3.t3Stop("homework3")
        t3.t3Stop("project name")
    

if __name__ == '__main__':
    unittest.main()