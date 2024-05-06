# M-122-Repo

## Gelerntes
### **Installation**
- Drücken Sie die Tasten 'WINDOWS' und 'R', um den Ausführen-Dialog zu öffnen.
- Geben Sie "optionalfeatures.exe" ein und bestätigen Sie.
- Aktivieren Sie "VM-Plattform", "Windows PowerShell 2.0" und "Windows-Subsystem für Linux (WSL)".
- Starten Sie das System neu.
- Im Microsoft Store wählen Sie "Ubuntu 22.04.1 LTS" aus.
- Merken Sie sich das Passwort, das Sie festlegen, da es nicht zurückgesetzt werden kann.
- Nach der Installation können Sie zwischen "CMD", "Ubuntu", "Powershell" und "WSL" wählen.
- Rechtsklick auf das gewünschte Fenster und "An Taskleiste anheften" für schnellen Zugriff.

### **Befehle Teil 1**

Linux bietet eine Vielzahl von Befehlen für die Shell, wie cp, alias, cat, rm, sowie Programmierstrukturen wie Schleifen und Verzweigungen. Diese können verwendet werden, um Systemaufgaben zu automatisieren.

Das Command Line Tool (Terminal) ermöglicht das Ausführen von Bash-Befehlen, wobei es einige Shortcuts gibt. Der Standard-Prompt kann geändert werden und zeigt üblicherweise den Benutzernamen, den Hostnamen und das aktuelle Verzeichnis an.

Tilde (~) steht für das Heimatverzeichnis des Benutzers, außer für den Administrator (root). Das Semikolon (;) trennt Befehle, das Pipe-Zeichen (|) verknüpft sie. Ein \ am Ende einer Zeile erlaubt es, den Befehl auf die nächste Zeile fortzusetzen. Ein & am Ende führt den Befehl im Hintergrund aus.

Die Befehle man, apropos und which helfen bei der Befehlssuche und Ortung von Programmen. Systemspezifische Befehle wie reboot, halt und Verzeichnisbefehle wie pwd, cd, mkdir, rmdir, ls, und find sind auch verfügbar.

Pfade können absolut (ab Root) oder relativ (ab aktuellem Verzeichnis) sein. Relevante Befehle wie cp, rm, mv, touch, cat, wc, und echo sowie Aliase und Wildcards erleichtern die Arbeit mit Dateien und Verzeichnissen.

### **Befehle Teil 2**

Erstellung eines Bash-Skripts: Der Prozess beginnt mit der Erstellung einer leeren Datei mit der Endung .sh und dem Hinzufügen des Shebangs (#!/bin/bash), um anzugeben, dass das Skript mit Bash ausgeführt werden soll.
Variablen: Es wird erklärt, wie Variablen in Bash erstellt, zugewiesen und verwendet werden. Die Lebensdauer von Variablen wird ebenfalls erläutert.
Automatisch verwaltete Variablen: Eine Liste der automatisch verwalteten Variablen von Bash wird bereitgestellt, einschliesslich Beispiele für ihre Verwendung.
Arithmetische Operatoren: Eine Einführung in arithmetische Operationen in Bash, einschliesslich der Verwendung der wichtigsten arithmetischen Operatoren.
Texteditoren: Empfohlene Texteditoren für die Bearbeitung von Bash-Skripten werden vorgestellt.
Ausgabeumleitung: Eine Erklärung zur Umleitung von Ein- und Ausgaben sowie zur Verwendung der Ausgabekanäle wird gegeben.
Pipeline: Die Verwendung von Pipelines zur Verarbeitung von textueller Ausgabe wird behandelt.
Fehlerbehandlung und Debugging: Tipps und Techniken zur Fehlerbehandlung und zum Debugging von Bash-Skripten werden präsentiert.

### **Befehle Teil 3**

Die Befehle chown und chmod werden verwendet, um den Eigentümer und die Zugriffsrechte einer Datei oder eines Verzeichnisses zu ändern.

Für die Verwaltung von Benutzern und Gruppen stehen verschiedene Befehle zur Verfügung, darunter useradd, userdel, passwd, logout, und su.

Zusätzlich zu den Befehlen für die Benutzerverwaltung gibt es auch eine Reihe von Werkzeugen zur Textverarbeitung in der BASH-Umgebung, wie grep, cut, sed, awk, curl und xargs, sowie die Möglichkeit, reguläre Ausdrücke zu verwenden.
