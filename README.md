This is a tool that reads out the time left in a match on the speakers of your driver station laptop

Demo:
https://www.youtube.com/shorts/bfsY4GpP0Tc

Installation instructions:
1. add this to your your teleop periodic:

``` SmartDashboard.putNumber("TimeLeft", DriverStation.getMatchTime()); ```

2. make a virtual env and install the requirements:
```
python -m venv .verbal
```
3. activate your python environment and run the script, this is what you should do before the match

```
.verbal/Scripts/activate
python app.py 10.TE.AM.2
```

4. turn up the volume on your laptop



To change which times are read edit the times_to_announce list in app.py
