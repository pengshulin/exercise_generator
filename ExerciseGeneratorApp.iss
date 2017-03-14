; Bearing monitor

[Setup]
AppName=自动出题机 V1.2
AppVersion=1.2
DefaultDirName={pf}\ExerciseGenerator
DefaultGroupName=自动出题机
DisableProgramGroupPage=yes
Compression=lzma2
SolidCompression=yes
OutputDir=app_dist
OutputBaseFilename=exercise_generator_setup_v1.2

[Files]
Source: "dist\*"; DestDir: "{app}"

[Icons]
Name: "{group}\自动出题机"; Filename: "{app}\ExerciseGeneratorApp.exe"
Name: "{group}\Uninstall"; Filename: "{uninstallexe}"
