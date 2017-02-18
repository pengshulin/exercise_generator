; Bearing monitor

[Setup]
AppName=自动出题机
AppVersion=1.0
DefaultDirName={pf}\ExerciseGenerator
DefaultGroupName=自动出题机
DisableProgramGroupPage=yes
Compression=lzma2
SolidCompression=yes
;UninstallDisplayIcon={app}\img\wang.ico
OutputDir=app_dist
OutputBaseFilename=exercise_generator_setup_v1.0

[Files]
Source: "dist\*"; DestDir: "{app}"

[Icons]
Name: "{group}\自动出题机"; Filename: "{app}\ExerciseGeneratorApp.exe"
Name: "{group}\Uninstall"; Filename: "{uninstallexe}"
