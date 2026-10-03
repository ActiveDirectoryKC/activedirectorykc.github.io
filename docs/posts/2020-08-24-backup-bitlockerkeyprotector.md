---
title: Cannot bind argument to parameter Exception because it is null with Backup-BitLockerKeyProtector
date: 2020-08-24
author: Tyler
tags: [windows, windows-server, bitlocker]
---

## Problem Statement

I have installed Bitlocker hundreds of times, literally. In fact, I’ve written a guide that my work uses and it has served us for years with no issues! However, I like to stretch myself from time-to-time. It is easy to follow instructions and do them without thought. It is a bit more challenging, at least, to try to do the install from memory and without a formal “How-To” guide. That’s where I am today.

I have a DC and a Management server in a lab environment hosted on Hyper-V. All is Server 2016. I enabled the vTPM, installed the Bitlocker feature, and enabled Bitlocker. When I attempt to run the command Backup-BitLockerKeyProtector I get an error, no matter how I do it

The error itself is very not helpful.

```
Write-Error : Cannot bind argument to parameter 'Exception' because it is null. At C:\Windows\system32\WindowsPowerShell\v1.0\Modules\BitLocker\BitLocker.psm1:2337 char:44     +                     Write-Error -Exception $ExceptionForHr     +                                            ~~~~~~~~~~~~~~~     + CategoryInfo          : InvalidData: (:) [Write-Error], ParameterBindingValidationException     + FullyQualifiedErrorId : ParameterArgumentValidationErrorNullNotAllowed,Microsoft.PowerShell.Commands.WriteErrorCommand
```

<!-- more -->

## Resolution for the Lazy

Just so you don’t have to read my whole analysis, the solution is to ensure you have correctly configured the BitLocker Group Policy setting to allow for backup to AD.

In my case it was “Computer Configuration \ Policies \ Administrative Templates \ Windows Components \ BitLocker Drive Encryption \ Operating System Drives” with the setting “Choose how BitLocker-protected operating system drives can be removed”.

## Detailed Analysis

It looks like the BitLocker module itself is throwing an error it cannot handle. I open the module up in PowerShell ISE (I know, I don’t have VSCode in this lab) and go to line 2337. I find that it is trying to do Write-Error with an exception. Microsoft designed a custom error lookup here and it is being called. For whatever reason it cannot handle it.

Walking back through the code I discover Microsoft is using a WMI Class (CIM Class) to do the BitLocker key backup. I change the code some, to fit my use case, and attempt to run it manually.

```powershell
$Vol = Get-CimInstance -Namespace "root\cimv2\Security\MicrosoftVolumeEncryption" -ClassName Win32_EncryptableVolume -ComputerName TESTER.TEST.CONTOSO.COM

Invoke-CimMethod -InputObject Vol -MethodName BackupRecoveryInformationToActiveDirectory -Arguments @{volumeKeyProtectorId = $ProtectorId} -ComputerName TESTER.TEST.CONTOSO.COM
```

When I run that, I get an output.

```
ReturnValue PSComputerName
----------- --------------
2147942487  TESTER.TEST.CONTOSO.COM
```

I had noticed at the top of the BitLocker.psm1 module that there were several error code constants. Interestingly, 2147942487 wasn’t one of them. I found some information on the “Encrypt method of the Win32_EncryptableVolume” class.

E_INVALIDARG 2147942487 (0x80070057): The EncryptionMethod parameter is provided but is not within the known range or does not match the current Group Policy setting.

The EncryptionMethod I chose was XtsAes256 which my Operating System version supports. I suspect the second half is the kicker; I haven’t configured the GPO.

I create and link a GPO with the correct setings and run the original command. It returns with the correct information that AD backed up my key.

```powershell
PS> Backup-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId $BLV.KeyProtector[1].KeyProtectorId
```

```
VolumeType Mount CapacityGB VolumeStatus Encryption KeyProtector AutoUnlock Protection
Point Percentage Enabled Status
---------- ----- ---------- ------------ ---------- ------------ ---------- ----------
OperatingSystem C: 79.45 FullyEncrypted 100 {Tpm, RecoveryPassword} On
```

I couldn’t find any documentation on the strict requirement of the GPO. Nonetheless, it fixed my issue. If I discover any supporting documentation, I will post it as an update.

Hope this all was informative and helpful!

## References

Backup-BitLockerKeyProtector
<https://docs.microsoft.com/en-us/powershell/module/bitlocker/backup-bitlockerkeyprotector?view=win10-ps>

Encrypt method of the Win32_EncryptableVolume class
<https://docs.microsoft.com/en-us/windows/win32/secprov/encrypt-win32-encryptablevolume>

GetEncryptionMethod method of the Win32_EncryptableVolumeClass
<https://docs.microsoft.com/en-us/windows/win32/secprov/getencryptionmethod-win32-encryptablevolume>
