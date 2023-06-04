#
# Gnuplot starten
#
gnuplot << EOF
#
# andern des default plotting style + postscript Einstellung fur eps
#
set terminal png
# Achsenbeschriftung
set xlabel "time (seconds) "
set ylabel "packets"
# Dateiname der Abbildung (Output)
set output "image.png"
# Separator festlegen fr die Inputdatei
# benutze ’,’ fr csv
set datafile separator ","
# Plot aus Dateien datei_1.log und datei_2.log
# datei_1: Spalte 1 f\ur die x-Achse und Spalte 7 fur die y-Achse
# datei_2: Zahlen 1 bis n f\ur die x-Achse und Spalte 2 fur die y-Achse
plot "gnuplot_test.txt" using 1:2 with lines title " test 1"
unset output
pause -1
EOF
