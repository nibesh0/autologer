[Setup]
AppName=AutoLoger
AppVersion=1.0
DefaultDirName={pf}\AutoLoger
OutputDir=Output
OutputBaseFilename=AutoLogerSetup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin
WizardImageFile=C:\Users\nibes\Source\Repos\autologer\res\icon.bmp
[Files]
Source: "C:\Users\nibes\Source\Repos\autologer\dist\cred.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\nibes\Source\Repos\autologer\dist\set.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\nibes\Source\Repos\autologer\res\*"; DestDir: "{app}\res"; Flags: ignoreversion recursesubdirs createallsubdirs

[Run]
Filename: "{app}\cred.exe"; Description: "Run cred.exe"; Flags: nowait postinstall runascurrentuser

[Tasks]
Name: "registryTask"; Description: "Add AutoLoger to Registry"; GroupDescription: "Additional Tasks";

[Registry]
Root: HKLM; Subkey: "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "AutoLoger"; ValueData: "{app}\set.exe"
Root: HKCU; Subkey: "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "AutoLoger"; ValueData: "{app}\set.exe"

[Code]
function GetKey(Param: String): String;
var
  KeyInput: TInputQueryWizardPage;
begin
  KeyInput := CreateInputQueryPage(wpSelectTasks, 'Choose a Profile Name', 'This name will be used as your Profile Name', 'Please specify a name to be used as your Profile Name (make sure it''s unique), then click Next.');
  KeyInput.Add('Key:', False);
  Result := KeyInput.Values[0];
end;
