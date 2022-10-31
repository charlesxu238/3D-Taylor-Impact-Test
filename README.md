# 3D-Taylor-Impact-Test
A script that writes ABAQUS input files for a working 3D taylor impact test

The test_vol data needs to either be added to the same directory as the script or just rewritten during the input to point to where your data is located
The script only looks for duplicate nodes and deletes them while rewriting the changes to the elements affected

The test merge that is in the folder is a working 3D taylor impact test
>All you need to do is create a job and run it
