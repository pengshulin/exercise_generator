; 

[Setup]
AppName=自动出题机 V1.4
AppVersion=1.4
DefaultDirName={pf}\ExerciseGenerator
DefaultGroupName=自动出题机
DisableProgramGroupPage=yes
Compression=lzma2
SolidCompression=yes
OutputDir=app_dist
OutputBaseFilename=exercise_generator_setup_v1.4

[Files]
Source: "dist\*"; DestDir: "{app}"

[Icons]
Name: "{group}\自动出题机"; Filename: "{app}\ExerciseGeneratorApp.exe"
Name: "{group}\Uninstall"; Filename: "{uninstallexe}"
