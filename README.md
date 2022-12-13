# smooth_gombocs

Dies ist das offizielle GitHub-Repository zur BeLL "Über die Existenz glatter Gömböcs" von Martin Wille.

Sie können diese Dateien downloaden und mit einer aktuellen Python-Installation (Version 3.9) ausführen.
Dafür benötigen Sie allerdings eine Installation der "open3d"-Bibliothek für Python.
Diese können Sie mithilfe einer Kommandozeile ihrer Wahl mit dem Befehl "pip install open3d" erhalten.

Wenn Sie "heightfield.py" ausführen, werden Sie zur Eingabe der Parameter c und d aufgefordert. Daraus wird die Heightfield-Datei "heightfield1.txt" erstellt sowie eine XYZ-Datei namens "test.xyz".
Führen Sie dann "visualizer.py" aus, wird Ihnen die generierte Punktwolke angezeigt.
Zu einer grafischen Auswertung bezüglich lokaler Maxima und Minima der generierten Oberfläche führen Sie anschließend "gradientfield.py" aus, welches daraufhin ein Gradientfeld anzeigt.

Falls Sie selbst Erfahrungen mit Python besitzen, können Sie die Dateien auch direkt modifizieren, um beispielsweise verschiedene Heightfields unter unterschiedlichen Dateinamen zu speichern.

Martin Wille
